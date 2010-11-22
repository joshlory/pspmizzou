from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from events.models import Event, EventCalendar

from datetime import datetime

def view_event(request, event_id):
    #return HttpResponse("event detail view: " + event_id)
    context = RequestContext(request, {})
    event = Event.objects.get(id=event_id)
    #event = query.fetch(limit=1)
    context['event'] = event
    return render_to_response("view_event.html", context)

def view_events_overview(request):
    context = RequestContext(request, {})
    now = datetime.now()
    month_events = Event.objects \
        .filter(start_datetime__gte=datetime(now.year, now.month, 1)) \
        .filter(start_datetime__lt=datetime(now.year, now.month + 1, 1))
    cal = EventCalendar(month_events)
    now = datetime.now()
    context['calendar'] = cal.formatmonth(now.year, now.month)
    events = Event.objects.order_by("start_datetime")[:50] # limit 50
    if events != None:
        context['events'] = []
        for event in events:
            context['events'].append(event)
    return render_to_response("events_overview.html", context)

def view_committee_events(request, committee):
    context = RequestContext(request, {})
    events = Event.objects.filter(committee=committee).order_by("start_datetime")
    context['committee'] = committee
    if events != None:
        context['events'] = []
        for event in events:
            context['events'].append(event)
    return render_to_response("committee_events.html", context)
