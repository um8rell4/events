from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginForm
from django.contrib.auth.views import LoginView


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
            return redirect(to='events:events')

        return render(request, self.template_name, {'form': form})


class CustomLogin(LoginView):
    authentication_form = LoginForm
    redirect_authenticated_user = '/'
# Create your views here.
