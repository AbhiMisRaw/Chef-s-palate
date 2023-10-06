from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {name}, your account is created')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request , 'user/register.html',{'form':form})

@login_required
def profilepage(request):
    return render(request , 'user/profile.html')
