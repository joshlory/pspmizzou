from django.http import HttpResponse

def view_committees_overview(request):
    return HttpResponse("committees overview")

def view_committee(request, committee):
    return HttpResponse(committee + " detail view")
