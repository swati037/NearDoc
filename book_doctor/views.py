import jwt
import requests
import json
from time import time
from pydoc import Doc
import reb

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from login.models import log, logd
import datetime

from book_doctor.models import Doctor, VidDoc, VidApp,  VAppointment
# Create your views here.

def search_doc(request):
    locs = Doctor.objects.values('location').distinct()
    spcs = Doctor.objects.values('specialist').distinct()
    return render(request, 'search_doc.html', {'locs' : locs, 'spcs' : spcs})

def select_date(request):
    location = request.POST['location']
    speciality = request.POST['specialist']
    docts = Doctor.objects.filter(location = location).filter(specialist = speciality)
    
    return render(request, 'select_date.html', {'docts' : docts})

def select_slot(request):
    if 'Video_Consult' in request.POST:
        dc = str(request.POST['doctor'])
        vdc = VidDoc.objects.filter(doctor__name = dc)
        print(vdc)
        slot = []
        for vidc in vdc:
            slot = VidApp.objects.filter(viddoc = vidc)

        newDate1 = str(datetime.date.today() + datetime.timedelta(days=0))
        newDate2 = str(datetime.date.today() + datetime.timedelta(days=1))
        date = [newDate1, newDate2]
        users = log.objects.all()
        
        return render(request, 'select_slot.html', {'slot' : slot, 'vdc' : vdc, 'date' : date, 'users' : users})
    else:
        return render(request, 'index.html')

def vid_details(request):
    dname = request.POST['dname']
    date = request.POST['date']
    tslot = request.POST['tslot']
    dc = Doctor.objects.get(name = dname)
    user = log.objects.get(email = request.session['email'])

    return render(request, 'vid_details.html', { 'user' : user, 'doc' : dc, 'date' : date, 'tslot' : tslot})

def vd_mpay(request):
    docname = request.POST['docname']
    uname = request.POST['uname']
    tslot = request.POST['tslot']
    date = request.POST['date']
    print(docname)
    print('----------------------------------------------------')
    doc = Doctor.objects.get(name = docname)
    user = log.objects.get(username = uname)
    zoom = createMeeting()
    appointment = VAppointment(doctor = doc, log = user, tslot = tslot, date = date, link = zoom[0], pword = zoom[1])
    appointment.save()
    # obj = VAppointment.objects.get(log__username = uname, doctor = doc, tslot = tslot, date = date)
    user = log.objects.get(email = request.session['email'])
    return render(request, 'com_payment.html', {'user' : user})




# Enter your API key and your API secret
API_KEY = '8weIgdIDSP-3AXfU2JjWiQ'
API_SEC = 'prZfLum67dSX3Q77GOKZXX8KnEAlQ56eRXEm'

# create a function to generate a token
# using the pyjwt library
def generateToken():
    token = jwt.encode(
    
    # Create a payload of the token containing
    # API Key & expiration time
    {'iss': API_KEY, 'exp': time() + 5000},
    
    # Secret used to generate token signature
    API_SEC,
    
    # Specify the hashing alg
    algorithm='HS256'
    )
    return token


# create json data for post requests
meetingdetails = {"topic": "The title of your zoom meeting",
            "type": 2,
            "start_time": "2019-06-14T10: 21: 57",
            "duration": "45",
            "timezone": "Europe/Madrid",
            "agenda": "test",

            "recurrence": {"type": 1,
                            "repeat_interval": 1
                            },
            "settings": {"host_video": "true",
                        "participant_video": "true",
                        "join_before_host": "False",
                        "mute_upon_entry": "False",
                        "watermark": "true",
                        "audio": "voip",
                        "auto_recording": "cloud"
                        }
            }

# send a request with headers including
# a token and meeting details
def createMeeting():
    headers = {'authorization': 'Bearer %s' % generateToken(),
        'content-type': 'application/json'}
    r = requests.post(
    f'https://api.zoom.us/v2/users/me/meetings',
    headers=headers, data=json.dumps(meetingdetails))

    print("\n creating zoom meeting ... \n")
    # print(r.text)
    # converting the output into json and extracting the details
    y = json.loads(r.text)

    join_URL = y["join_url"]
    meetingPassword = y["password"]
    zoom = [join_URL, meetingPassword]
    print(f'\n here is your zoom meeting link {join_URL} and your \
    password: "{meetingPassword}"\n')
    return zoom

# run the create meeting function
# createMeeting()