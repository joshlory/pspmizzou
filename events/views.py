from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from events.models import Event, EventCalendar

from datetime import datetime

def view_event(request, event_id):
    #return HttpResponse("event detail view: " + event_id)
    context = RequestContext(request, {})
    event = Event.get(event_id)
    #event = query.fetch(limit=1)
    context['event'] = event
    return render_to_response("view_event.html", context)

def view_events_overview(request):
    context = RequestContext(request, {})
    now = datetime.now()
    month_query = Event.all() \
        .filter("start_datetime >=", datetime(now.year, now.month, 1)) \
        .filter("start_datetime <", datetime(now.year, now.month + 1, 1))
    month_events = month_query.fetch(limit=40)
    cal = EventCalendar(month_events)
    now = datetime.now()
    context['calendar'] = cal.formatmonth(now.year, now.month)
    query = Event.all().order("start_datetime")
    events = query.fetch(limit=40)
    if events != None:
        context['events'] = []
        for event in events:
            context['events'].append(event)
    return render_to_response("events_overview.html", context)

def view_committee_events(request, committee):
    context = RequestContext(request, {})
    events = Event.all().filter("committee", committee).order("start_datetime")
    context['committee'] = committee
    if events != None:
        context['events'] = []
        for event in events.fetch(limit=40):
            context['events'].append(event)
    return render_to_response("committee_events.html", context)
