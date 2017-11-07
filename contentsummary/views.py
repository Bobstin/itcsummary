from django.shortcuts import render

import pdb

from .models import Session, Quote, KeyTakeaway, Speech

# Create your views here.
def example(request):
	return render(request,'contentsummary/example.html')

def nextSession(request):
	#print('hello')
	return render(request,'contentsummary/nextSession.html')

def singleSession(request,session_number):
	#pdb.set_trace()
	session = Session.objects.get(number=session_number)

	context = {
	'session':session,
	'quotes':Quote.objects.filter(session=session),
	'keytakeaways':KeyTakeaway.objects.filter(session=session),
	'speakers':Speech.objects.filter(session=session),
	}

	return render(request,'contentsummary/example_auto_no_resize.html',context)
	


	
