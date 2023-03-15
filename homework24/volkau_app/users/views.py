from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from .forms import CustomUserForm, PasswordChangeForm,UserUpdateForm, ProfileUpdateForm
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
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
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
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)