from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from projects.models import Task
from .models import UserProfile
from .models import Invite
from .forms import RegistrationForm
from .forms import TeamRegistrationForm
from .forms import ProfilePictureForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
# Create your views here.
def register(request):
    if request.method == 'POST':
        form1 = AuthenticationForm()
        form = RegistrationForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            user = form.save()
            created = True
           # login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            context = {'created' : created}
            return render(request, 'register/login.html',{'login_form':form1})
        else:
            return render(request, 'register/reg_form.html', context)
    else:
        form = RegistrationForm()
        context = {
            'form' : form,
        }
        return render(request, 'register/reg_form.html', context)


def usersView(request):
    users = UserProfile.objects.all()
    tasks = Task.objects.all()
    #tasks=request.user.tasks
    context = {
        'users': users,
        'tasks': tasks,
    }
    return render(request, 'register/users.html', context)

def user_view(request, profile_id):
    user = UserProfile.objects.get(id=profile_id)


    context = {
        'user_view' : user,
    }
    user2 = UserProfile.objects.get(user=request.user)
    if user2.type == 'Leader':
        return render(request, 'register/user.html', context)
    else:
        return render(request, 'register/usermember.html', context)
