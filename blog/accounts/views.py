from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

from blog_app.models import Article


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "That username is taken")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "That email is being used")
                    return redirect("register")
                else:
                    user = User.objects.create_user(
                        username=username, password=password, email=email
                    )
                    user.save()
                    messages.success(request, "You are now registered and can log in")
                    return redirect("login")
        else:
            messages.error(request, "Passwords do not match")
            return redirect("register")
    else:
        return render(request, "accounts/register.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login")
    else:
        return render(request, "accounts/login.html")


def logout(request):
    auth.logout(request)
    return redirect("home")


def dashboard(request):
    user_articles = Article.objects.filter(author=request.user.id).order_by(
        "-created_on"
    )

    context = {"articles": user_articles}
    return render(request, "accounts/dashboard.html", context)
