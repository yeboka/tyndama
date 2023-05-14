from django.shortcuts import render
from .models import Music
from mutagen.mp3 import MP3


def home(request):
    music = Music.objects.all()

    return render(request, 'tyndama/home.html', {'music' : music})


def get_music(request):
    music = Music.objects.all()
    for i in music:
        name = str(i.song)
        audio_path = './media/' + name
        print('this is url:: '+audio_path)
        audio = MP3(audio_path)
        length=int(audio.info.length)
        print(length)

    return render(request, 'tyndama/get_music.html', {'music': music})