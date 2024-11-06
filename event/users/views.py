from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginForm, EditUserForm, EditUserProfileForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class SignupView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    initial = None
    template_name = 'registration/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='events:events')
        
        return super(SignupView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *arg, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect(to='users:login')

        return render(request, self.template_name, {'form': form})


class CustomLogin(LoginView):
    authentication_form = LoginForm
    redirect_authenticated_user = '/'


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users/user_profile.html', {'user': user})


@login_required
def user_profile_edit(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        profile_form = EditUserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect(to='users:user_profile', username=request.user)
    else:
        form = EditUserForm(instance=request.user)
        profile_form = EditUserProfileForm(instance=request.user)

    return render(request, 'users/user_profile_edit.html', {'user_form': form,
                                                            'user_profile_form': profile_form})


@login_required
def delete_profile(request):
    user = get_object_or_404(User, username=request.user)
    if request.method == 'POST':
        user.delete()
        return redirect(to='users:login')
    return render(request, 'users/delete_profile.html')
# Create your views here.
