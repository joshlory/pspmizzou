from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

def view_index(request):
    context = RequestContext(request, {})
    return render_to_response("index.html", context)

def view_login(request):
    username = request.POST['user']
    password = request.POST['pass']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            if request.GET.has_key('next'):
                return redirect(request.GET['next'])
            return redirect('/')
        else:
            # Return a 'disabled account' error message
            return HttpResponse("Error: Account disabled.")
    else:
        return HttpResponse("Error: Login failed.") # TODO: Need a login template

def view_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
    return HttpResponse("TODO: Logout form.") # TODO: Need a logout template
