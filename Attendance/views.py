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
        'logged_in':request.user.is_authenticated(),
    }
    return render(request, 'attendance/home.html', context)

@require_http_methods(["GET", "POST"])
def web_login(request):
    if request.method == "POST":
        perform_login(request)
        return redirect('attendance:home')
    else:
        context = {
            'title':'Login',
            'logged_in':request.user.is_authenticated(),
        }
        return render(request, 'attendance/login.html', context)

def perform_login(request):
    if request.POST.has_key("username") and request.POST.has_key("password"):
        if not request.user.is_authenticated():
            user = authenticate(username=request.POST["username"], password=request.POST["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Successfully logged in as '+user.username+'!')
                else:
                    messages.error(request, 'User account '+user.username+' is disabled.')
            else:
                messages.error(request, 'Invalid username or password.')
        
        else:
            messages.warning(request, 'Already logged in as '+request.user.username+'.')
    else:
        messages.warning(request, 'Invalid post request.')

def web_logout(request):
    if request.user.is_authenticated():
        old_user = request.user.username
        logout(request)
        messages.success(request, 'Successfully logged out user '+old_user+'.')
    return redirect('attendance:home')

