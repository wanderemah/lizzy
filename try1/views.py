from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from church.models import signUp, Message, New


def home(request):
    message = Message.objects.all()
    news = New.objects.all()
    return render(request, 'home.html', {'message': message, "news": news})


@login_required
def base(request, username):
    user = signUp.objects.get(user__username=username)
    return render(request, 'base.html', {'user': user, 'username': username})



def about(request):
    return render(request, 'about.html')


@login_required
def about2(request, username):
    user = signUp.objects.get(user__username=username)
    return render(request, 'about2.html', {'user': user, 'username': username})


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=user_name, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('base', kwargs={'username': user_name}))
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html', {'form': login})


@login_required
def contacts(request, username):
    user = signUp.objects.get(user__username=username)
    return render(request, 'contacts.html', {'username': username, 'user': user})


def contacts2(request):
    return render(request, 'contacts2.html')
