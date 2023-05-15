from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Music, Playlist
from mutagen.mp3 import MP3
from django.contrib.auth import authenticate, login, logout
from tyndama.forms import CreateUserForm, AddMusicForm, PlaylistForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import User



@login_required(login_url=login)
def home(request):
    music = Music.objects.all()
    playlist = Playlist.objects.filter(user=request.user)

    return render(request, 'tyndama/home.html', {'music': music, 'playlist': playlist})


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
            if user.is_superuser:
                # User is a superuser
                login(request, user)
                return redirect('admin_panel')
            else:
                # User is a regular user
                login(request, user)
                return redirect('user_profile')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, "tyndama/loginPage.html", context)


def logoutPage(request):
    logout(request)
    return redirect('home')


def user_profile(request):
    playlist = Playlist.objects.filter(user=request.user)
    context = {'playlist': playlist}
    return render(request, 'tyndama/user_profile.html', context)


def admin_panel(request):
    music = Music.objects.all()
    if request.user.is_authenticated:
        if request.user.is_superuser:
            context = {'music': music}
            return render(request, 'tyndama/admin_panel.html', context)
    else:
        return redirect('home')



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



def add_playlist(request):
    music_items = Music.objects.all()
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            print('form is valid')
            playlist = form.save(commit=False)
            playlist.user = request.user
            playlist.save()
            form.save_m2m()
            return redirect('playlist', playlist.id)
    else:
        print('sory you can not add')
        form = PlaylistForm()
    return render(request, 'tyndama/add_playlist.html', {'form': form, 'music_items': music_items})


def playlist_detail(request, playlist_id):
    all_playlist = Playlist.objects.filter(user=request.user)

    playlist = Playlist.objects.get(id=playlist_id)
    music_list = playlist.songs.all()
    return render(request, 'tyndama/playlist.html', {'music': music_list, 'playlist': all_playlist, 'curr_playlist': playlist})

def delete_music(request, pk):
    music = Music.objects.get(song_id=pk)
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'POST':
                music.delete()
                return redirect('home')
    else:
       context = {'music': music}
       return render(request, 'tyndama/delete_music.html', context)


