from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect

from .forms import SignUpForm

# Create your views here.
def signin(request):
    return render(request, 'signin.html')

def signout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:signin'))

def redirect_view(request):
    return redirect('signin/')

def signup(request):
    if request.method != 'POST':
        form = SignUpForm()
    else:
        form = SignUpForm(request.POST)
    
    if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('users:signin'))
    
    context = {'form': form}
    return render(request, 'signup.html',context)