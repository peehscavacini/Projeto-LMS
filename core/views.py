from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from app.models import *
from datetime import datetime


def home(request):
	assert isinstance(request, HttpRequest)
	return render(
		request, 
		'index.html',
        context_instance = RequestContext(request,
        {
            'year':datetime.now().year,
        })
    )
    

