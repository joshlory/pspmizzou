from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

def view_index(request):
    context = RequestContext(request, {})
    return render_to_response("index.html", context)

def view_login(request):
    context = RequestContext(request, {})
    context['next'] = (request.GET['next'] if request.GET.has_key('next') else "/")
    # If the user is already logged in: redirect to destination
    if request.user.is_authenticated():
        return redirect(context['next'])
    # No post data: show login view
    if request.method != "POST":
        return render_to_response("login.html", context)
    # Otherwise handle post data
    username = request.POST['user']
    password = request.POST['pass']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active: # Successful login
            login(request, user)
            return redirect(context['next'])
        else: # Account disabled
            context['disabled'] = True
            return render_to_response("login.html", context)
    else: # Wrong username/password
        context['failed'] = True
        return render_to_response("login.html", context)

def view_logout(request):
    if not request.user.is_authenticated():
        return redirect(view_login)
    if request.method == "POST":
        logout(request)
        return redirect("/")
    context = RequestContext(request, {})
    return render_to_response("logout.html", context)
