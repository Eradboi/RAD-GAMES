from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def login_view(request):
    error = None
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('games:home')
        else:
            error = 'Invalid username or password'
    else:
        form = AuthenticationForm(request)
    return render(request, 'login/login.html', { 'form': form, 'error':error})

def handling_404(request, exception):
    return render(request, 'login/404.html', {})

def error_500(request):
    return render(request, "login/500.html",{})