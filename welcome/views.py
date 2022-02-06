from django.shortcuts import render
from django.contrib.auth import get_user_model


# Create your views here.
def index(request):
    return render(request, 'welcome/welcome_base.html')


def show_all_users(request):
    user_model = get_user_model()
    list_of_users = user_model.objects.all()
    context = {
        'list_of_users': list_of_users,
    }
    return render(request, 'welcome/show_all_users.html', context)
