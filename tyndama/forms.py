from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Music


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)

        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

        user.email = self.cleaned_data[email]
        if commit:
            user.save()
        return user




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