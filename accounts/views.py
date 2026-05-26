from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2 and len(password) >= 6:
            User.objects.create_user(username=username, password=password)
            return redirect('accounts:profile')
    
    return render(request, 'accounts/register.html')
@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})