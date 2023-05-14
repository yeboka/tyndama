from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Music
from mutagen.mp3 import MP3
from django.contrib.auth import authenticate, login, logout
from tyndama.forms import CreateUserForm, AddMusicForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import User


from django.contrib.auth.models import User




def home(request):
    music = Music.objects.all()

    return render(request, 'tyndama/home.html', {'music': music})


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'tyndama/registerPage.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('user_profile')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, "tyndama/loginPage.html", context)

def logoutPage(request):
    logout(request)
    return redirect('login')
@login_required(login_url=login)
def user_profile(request):

    context = {}
    return render(request, 'tyndama/user_profile.html', context)

def get_music(request):
    music = Music.objects.all()
    for i in music:
        name = str(i.song)
        audio_path = './media/' + name
        # print('this is url:: '+audio_path)
        get_time(name, audio_path)

    return render(request, 'tyndama/get_music.html', {'music': music})


def get_time(name, url):
    # audio_path = './media/' + name
    print('this is url:: ' + url)
    audio = MP3(url)
    length = int(audio.info.length)
    print(length)


def add_music(request):
    form = AddMusicForm()
    if request.method == 'POST':
        form = AddMusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form is valid!')
            return HttpResponseRedirect('/')
        else:
            print('error')
    context = {'form': form}
    return render(request, 'tyndama/add_music.html', context=context)
