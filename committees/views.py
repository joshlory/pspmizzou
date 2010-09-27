from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def view_committees_overview(request):
    context = RequestContext(request, {})
    return render_to_response("committees_overview.html", context)

def view_committee(request, committee):
    return HttpResponse(committee + " detail view")
