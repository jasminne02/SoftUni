from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views, authenticate, login, get_user_model
from django.urls import reverse_lazy

from UserAndPasswordManagement.web.forms import CustomUserCreationForm
from django.views import generic


UserModel = get_user_model()


def home_view(request):
    return render(request, 'home.html')


class UserRegistrationView(generic.CreateView):
    form_class = CustomUserCreationForm()
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['profile_form'] = CustomUserCreationForm()
        return context


class CustomLoginView(views.LoginView):
    template_name = 'login.html'


class CustomLogoutView(views.LogoutView):
    pass


def register_view(request):
    if request.method == 'GET':
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'register.html', context)


def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = UserModel.objects.get(username=username)
    login(request, user)



