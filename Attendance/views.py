from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from Attendance.models import Organization, Meeting, AttendanceRecord

# Create your views here.

def index(request):
    context = {
        'title':'Home',
        'user':request.user,
        'logged_in':request.user.is_authenticated(),
    }
    if context['logged_in']:
        context['admin_orgs'] = request.user.admin_of_set.all()
    return render(request, 'attendance/home.html', context)

@require_http_methods(["GET", "POST"])
def web_login(request):
    if request.method == "POST":
        return perform_login(request)
    else:
        context = {
            'title':'Login',
            'logged_in':request.user.is_authenticated(),
        }
        return render(request, 'attendance/login.html', context)

def perform_login(request):
    context = {
        'title':'Login',
        'logged_in':request.user.is_authenticated(),
        'retry':True,
        'username':request.POST["username"],
        'password':request.POST["password"],
    }
    if request.POST.has_key("username") and request.POST.has_key("password"):
        if not request.user.is_authenticated():
            user = authenticate(username=request.POST["username"], password=request.POST["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Successfully logged in as '+user.username+'!')
                else:
                    messages.error(request, 'User account '+user.username+' is disabled.')
                    return render(request, 'attendance/login.html', context)
            else:
                messages.error(request, 'Invalid username or password.')
                return render(request, 'attendance/login.html', context)
        else:
            messages.warning(request, 'Already logged in as '+request.user.username+'.')
    else:
        messages.warning(request, 'Invalid post request.')
    return redirect('attendance:home')

def web_logout(request):
    if request.user.is_authenticated():
        old_user = request.user.username
        logout(request)
        messages.success(request, 'Successfully logged out user '+old_user+'.')
    return redirect('attendance:home')

#@require_http_methods(["POST"])
def mcc_api(request):
    return HttpResponse("received beacon data")
