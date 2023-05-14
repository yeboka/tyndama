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

def user_profile(request):

    context = {}
    return render(request, 'tyndama/user_profile.html', context)

def get_music(request):
    music = Music.objects.all()
    for i in music:
        name = str(i.song)
        audio_path = './media/' + name
        print('this is url:: ' + audio_path)
        audio = MP3(audio_path)
        length = int(audio.info.length)
        print(length)


    return render(request, 'tyndama/get_music.html', {'music': music})






def add_music(request):
    form = AddMusicForm()
    if request.method == 'POST':
        form = AddMusicForm(request.POST, request.FILES)

        if form.is_valid():
            print("Hi")
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Form is valid!')
            return HttpResponseRedirect('/')
        else:
            print('error')
    context = {'form': form}
    return render(request, 'tyndama/add_music.html', context=context)
