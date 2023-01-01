from django.db.models import Avg
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.urls import reverse
from django.http import HttpResponseRedirect
from register.models import Team
from register.models import Project
from register.models import UserProfile
from projects.models import Task

# Create your views here.
def index(request):
    user2=UserProfile.objects.get(user=request.user)
    if user2.type=="Leader":
        return render(request, 'core/index.html')
    elif user2.type=="Members":
        projects = Project.objects.all().filter(assign=request.user)
        avg_projects = Project.objects.all().aggregate(Avg('complete_per'))['complete_per__avg']
        tasks = Task.objects.all()
        overdue_tasks = tasks.filter(due='2')
        context = {
            'avg_projects': avg_projects,
            'projects': projects,
            'tasks': tasks,
            'overdue_tasks': overdue_tasks,
        }
        return render(request, 'projects/projectsmember.html',context)


def dashboard(request):
    users = User.objects.all()
    active_users = User.objects.all().filter(is_active=True)
    teams = Team.objects.all()
    projects = Project.objects.all()
    tasks = Task.objects.all()
    context = {
        'users' : users,
        'active_users' : active_users,
        'teams' : teams,
        'projects' : projects,
        'tasks' : tasks,
    }
    return render(request, 'core/dashboard.html', context)



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, authenticated_user)
            return redirect('core:index')
        else:
            return render(request, 'register/login.html', {'login_form':form})
    else:
        form = AuthenticationForm()
    return render(request, 'register/login.html', {'login_form':form})




