from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template 
from django.template import Context
from datetime import datetime
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from bigbrother.zenoss import api, texttable
import curses
import time


def main():
    # Initialize Zenoss API connection
    z = api.ZenossAPIExample()
    rawEvents = z.get_events()['events']
    events = []
    colors = []
    for x in rawEvents:
        # Iterate through raw event data, and pull the rows we want
        events.append([x['device']['text'], x['component']['text'],
                        x['summary'], x['eventClass']['text']])
    # 'Clean' events list, initialized with title row
    return events

def monitoring(request, center):
    return render_to_response('center.html', locals())

def dashboard(request):
    table = main()
    return render_to_response('dashboard.html', locals())

def hola(request):
    return HttpResponse("Hola mundo")