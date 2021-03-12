from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.author = request.user
            new_user.save()
            messages.success(request, f'Hi {new_user.author.username.title()}, you can now log in to your account ')
            return redirect('users:login')
    context = {
        'form' : form
    }
    return render(request, 'registration/register.html', context)

