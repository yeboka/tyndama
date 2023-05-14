from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Music
from mutagen.mp3 import MP3
from django.contrib.auth import authenticate, login, logout
from tyndama.forms import CreateUserForm, AddMusicForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    music = Music.objects.all()

    return render(request, 'tyndama/home.html', {'music' : music})

def registerPage(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = CreateUserForm()
    context = {'form': form}
    return render(request, 'tyndama/registerPage.html', context)


def loginPage(request):
    login_form = AuthenticationForm()
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    context = {"login_form": login_form}
    return render(request=request, template_name="tyndama/loginPage.html", context=context)


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
    submitted = False
    form = AddMusicForm()

    if 'submitted' in request.GET:
        submitted = True

    if request.method == 'POST':
        form = AddMusicForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_music?submitted=True')
        else:
            submitted = True
    context = {'form': form, 'submitted': submitted}
    return render(request, 'tyndama/add_music.html', context)

