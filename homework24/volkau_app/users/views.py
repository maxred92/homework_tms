from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from .forms import CustomUserForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, "users/register.html", {'form': CustomUserForm})
    elif request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('store:index'))
        else:
            form = CustomUserForm(request.POST)
        return render(request, 'users/register.html', {'form': form})


class CustomPasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name='users/password_change.html'
    success_url = reverse_lazy('users:password_change_done')

    def form_valid(self, form):
        form.save()
        self.request.session.flush()
        logout(self.request)
        return super().form_valid(form)

@login_required
def profile(request):
    return render(request, 'users/profile.html')