from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password

from .models import User
from .forms import RegisterForm
from blog.models import Post, Category
from game.models import Game


def userInfo(request):
    posts = Post.objects.filter(author=request.user.pk).order_by("-createTime")
    games = Game.objects.filter(author=request.user.pk).order_by("-createTime")
    context = {
        'posts': posts,
        'games': games
    }
    return render(request, 'account/user.html',context=context)


def register(request):
    redirect_to = request.POST.get("next", request.GET.get('next', ''))
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_name = request.POST.get("email", "")
            pass_word = request.POST.get("password", "")
            user_profile = User()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()
            send_register_email(user_name, "register")
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', context={'form': form, 'next': redirect_to})


def infoChange(request):
    user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        user.headphoto = request.FILES['headphoto']
        user.save()
        return redirect("/user/")
    return render(request, 'account/userInfo.html',context={})