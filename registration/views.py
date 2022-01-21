from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = RegisterForm()

        return render(request, "registration/sign_up.html", {"form": form})
