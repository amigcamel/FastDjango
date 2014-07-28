#-*-coding:utf-8-*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext

def index(request):
    message = 'Hello, Loper!'
    return render_to_response('index.html', {'message':message}, context_instance=RequestContext(request))

