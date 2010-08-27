from django.http import HttpResponse

def view_event(request, event_id):
    return HttpResponse("event detail view")

def view_events_overview(request):
    return HttpResponse("events overview view")
