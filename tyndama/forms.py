from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Music, Playlist


class CreateUserForm(UserCreationForm):
    username = forms.CharField(label='Log_in',
                               widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Username'}))
    email = forms.CharField(label='Email',
                            widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Email address'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'password first'}))
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'password second'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# create music form
class AddMusicForm(ModelForm):
    class Meta:
        model = Music
        fields = ('name', 'singer', 'tags', 'image', 'song', 'album')
        labels = {
            'name': '',
            'singer': '',
            'tags': '',
            'image': '',
            'song': '',
            'album': '',

        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'singer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Singer'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'song': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Song'}),
            'album': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Album'}),

        }


class PlaylistForm(forms.ModelForm):
    songs = forms.ModelMultipleChoiceField(
        queryset=Music.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'search-input'})
    )

    class Meta:
        model = Playlist
        fields = ['name', 'songs']