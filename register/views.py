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



def profile(request):
    if request.method == 'POST':
        img_form = ProfilePictureForm(request.POST, request.FILES)
        print('PRINT 1: ', img_form)
        context = {'img_form' : img_form }
        if img_form.is_valid():
            img_form.save(request)
            updated = True
            context = {'img_form' : img_form, 'updated' : updated }
            user2 = UserProfile.objects.get(user=request.user)
            if user2.type == 'Leader':
                return render(request, 'register/profile.html', context)
            else:
                return render(request, 'register/profilemember.html', context)

        else:

            user2 = UserProfile.objects.get(user=request.user)
            if user2.type == 'Leader':
                return render(request, 'register/profile.html', context)
            else:
                return render(request, 'register/profilemember.html', context)
    else:
        img_form = ProfilePictureForm()
        context = {'img_form' : img_form }
        user2 = UserProfile.objects.get(user=request.user)
        if user2.type == 'Leader':
            return render(request, 'register/profile.html', context)
        else:
            return render(request, 'register/profilemember.html', context)


def newTeam(request):
    if request.method == 'POST':
        form = TeamRegistrationForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            form.save()
            created = True
            form = TeamRegistrationForm()
            context = {
                'created' : created,
                'form' : form,
                       }
            return render(request, 'register/new_team.html', context)
        else:
            return render(request, 'register/new_team.html', context)
    else:
        form = TeamRegistrationForm()
        context = {
            'form' : form,
        }
        return render(request, 'register/new_team.html', context)


def invites(request):
    user2 = UserProfile.objects.get(user=request.user)
    if user2.type == 'Leader':
        return render(request, 'register/invites.html')
    else:
        return render(request, 'register/invitesmember.html')



def invite(request, profile_id):
    profile_to_invite = UserProfile.objects.get(id=profile_id)
    logged_profile = get_active_profile(request)
    if not profile_to_invite in logged_profile.friends.all():
        logged_profile.invite(profile_to_invite)
    return redirect('core:index')


def deleteInvite(request, invite_id):
    logged_user = get_active_profile(request)
    logged_user.received_invites.get(id=invite_id).delete()
    return render(request, 'register/invites.html')


def acceptInvite(request, invite_id):
    invite = Invite.objects.get(id=invite_id)
    invite.accept()
    return redirect('register:invites')

def remove_friend(request, profile_id):
    user = get_active_profile(request)
    user.remove_friend(profile_id)
    return redirect('register:friends')


def get_active_profile(request):
    user_id = request.user.userprofile_set.values_list()[0][0]
    return UserProfile.objects.get(id=user_id)


def friends(request):
    if request.user.is_authenticated:
        user = get_active_profile(request)
        friends = user.friends.all()
        context = {
            'friends' : friends,
        }
    else:
        users_prof = UserProfile.objects.all()
        context= {
            'users_prof' : users_prof,
        }
    user2 = UserProfile.objects.get(user=request.user)
    if user2.type=='Leader':
        return render(request, 'register/friends.html', context)
    else:
        return render(request, 'register/friendsmember.html', context)
