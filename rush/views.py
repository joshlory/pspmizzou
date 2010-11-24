from django.shortcuts import render_to_response
from django.template import RequestContext

def view_rush_overview(request):
    context = RequestContext(request, {})
    return render_to_response("rush_overview.html", context)
