from django.shortcuts import render
from .models import Sensordata
import time
import sys

def index(request):
	data = Sensordata.objects.all().order_by('-sample_id')[:5]
	dl = len(data)
	return render(request, "SmartFarm/show.html",{"objects":data,"length":dl})

def more(request,sample_id):
	obj = Sensordata.objects.filter(pk = sample_id).first()
	print(obj.humidity)
	return render(request, "SmartFarm/more.html",{"object":obj})

def turnon(request):
	print("Turned on")

	blah = "This is written slowly\n"
	for l in blah:
		sys.stdout.write(l)
		sys.stdout.flush()
		time.sleep(0.6)
	pass
def turnoff(request):
	print("Turned off")
	blah = "This is written slowly\n"
	for l in blah:
		sys.stdout.write(l)
		sys.stdout.flush()
		time.sleep(0.6)
	pass
