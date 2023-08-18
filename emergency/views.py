from django.shortcuts import render
from .models import Container
import pyttsx3

# Create your views here.
def emerg(request):
    obj = Container.objects.all()
    # audiolist = []

    
    # for i in obj:
        # print(i.measures)
        
        # audio_obj = pyttsx3.init()
        
        # fo = open("G:\\DRIVES\\D_DRIVE\\MUSIC\\Tones\\Puneri.mp3", "r")
        # ip = fo.read()
        
        # audio = audio_obj.say(i.measures)
        # obj[i].audio = audio

        # obj.append(audio)
        # audiolist.append(audio)
        
        # audio = audio_obj.runAndWait()
        
    # print(obj[0].title)  
    # for j in range(3):
    #     obj[j].audio = audiolist[j] 
    
    # print([obj])
    
    # audio_obj.runAndWait()
    return render(request, 'emergency.html', {'obj':obj})