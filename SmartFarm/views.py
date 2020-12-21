from django.shortcuts import render
from .models import Sensordata
import sys
from subprocess import run,PIPE


def index(request):
	data = Sensordata.objects.all().order_by('-sample_id')[:5]
	dl = len(data)
	return render(request, "SmartFarm/show.html",{"objects":data,"length":dl})

def more(request,sample_id):
	obj = Sensordata.objects.filter(pk = sample_id).first()
	print(obj.humidity)
	return render(request, "SmartFarm/more.html",{"object":obj})

def turnonoff(request):
	onoff = request.GET.get("onoff")
	out = run([sys.executable,'//Users//kailash//Desktop//hello.py',onoff],shell = False, stdout = PIPE)

