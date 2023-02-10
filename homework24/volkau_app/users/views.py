from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUser


# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, "users/register.html", {'form': CustomUser})
    elif request.method == "POST":
        form = CustomUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('store:index'))
        else:
            form = CustomUser(request.POST)
        return render(request, 'users/register.html', {'form': form})
