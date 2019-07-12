from django.http import HttpResponse
from django.shortcuts import (
    render,
    redirect
)

from .forms import (
    UserLoginForm,
    UserRegisterForm,
)

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)


def home(request):
    # if request.user.is_authenticated:
    #     profile = blogPost.objects.filter(author=request.user)
    #     for i in profile:
    #         if i:
    #             return redirect('profile')
    return render(request, 'accounts/home.html')



def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        else:
            return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'accounts/login.html', context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit = False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        else:
            return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')

