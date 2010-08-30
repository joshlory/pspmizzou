from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template import loader, Context

from events.models import Event

def view_event(request, event_id):
    #return HttpResponse("event detail view: " + event_id)
    context = RequestContext(request, {})
    event = Event.get(event_id)
    #event = query.fetch(limit=1)
    context['event'] = event
    return render_to_response("view_event.html", context)

def view_events_overview(request):
    context = RequestContext(request, {})
    events = Event.all()
    if events.count(1) < 1:
        return HttpResponse("No events found.")
    context['events'] = []
    for event in events.fetch(limit=40):
        context['events'].append(event)
    return render_to_response("events_overview.html", context)
