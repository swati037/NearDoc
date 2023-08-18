# Generated by Django 3.1.7 on 2022-01-19 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoplabtest', '0008_orders_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
