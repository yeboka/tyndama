from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test


def is_admin(user):
    if user.is_superuser:
        return
    else:
        return redirect('home')


