# # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.contrib.auth.models import Group, Permission
from organizations.models import Organization
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import permission_required, user_passes_test
from organizations.forms import OrganizationUserCreateForm
from .forms import CustomUserCreateForm
from .models import CustomUser

"""
if not authenticated you can signup then redirect to home
"""
def mySignup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreateForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('/')
        else:
            form = CustomUserCreateForm()
        return render(request, 'signup.html', {'form': form})
    else :
        return redirect("/")

"""
# if not authenticated and is active user you can login.
# if Superuser or Staff redirect to myadmin page else to home page.
"""
def myLogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                if request.user.is_superuser or request.user.is_staff:
                    return redirect(reverse("users:myadmin"))
                else :
                    return redirect(reverse("home"))
            return redirect(reverse("users:login"))
        else:
            form = AuthenticationForm()
            context =  {'form': form}
        return render(request, 'registration/login.html',context)
    else :
        return redirect("/")

"""
# isStaff and isSuperuser is used in @user_passes_test decorators
"""
def isStaff(user):
    return True if user.is_staff or user.is_superuser else False
def isSuperuser(user):
    return True if user.is_superuser else False
def isOwner(user):
    return True if user.is_owner else False


"""
# if you are Staff you can enter  .
"""
@user_passes_test(isStaff , login_url = 'users:login')
def myadmin(request):
    context = {
    "users" : CustomUser.objects.all()
    }
    return render(request, 'admins/admin.html', context)

"""
# if you are Staff you can show users list.
"""
@user_passes_test(isStaff, login_url = 'users:login')
def users_list(request):
    users = CustomUser.objects.all()
    context = {
    "users" : users,
    }
    return render(request, "admins/users.html", context)

"""
show user profile
"""
def profile(request, pk):
    customuser = CustomUser.objects.get(id = pk)
    user_permissions  = customuser.user_permissions.all()
    context = {
    "customuser" : customuser,
    "user_permissions" : user_permissions
    }
    return render(request, "users/profile.html", context)

"""
the Owner of the same organization of that user
only who can edit users permissions
"""
@user_passes_test(isOwner, login_url = 'users:login')
def userEditPermissions(request, pk):
    user = CustomUser.objects.get(id = pk)
    user_organization = user.organization
    if request.user.organization == user_organization:
        # all permissions for organization
        all_permissions =  Permission.objects.filter(codename__contains="organization") # change with site permissions
        # user permissions
        user_permissions  = user.user_permissions.all()
        # create a list of permissions codename
        userPermList = []
        for user_perm in user_permissions :
            userPermList.append(user_perm.codename)
        allPermList = []
        for all_perm in all_permissions :
            allPermList.append(all_perm.codename)

        if request.method == "POST":
            # get a list of permissions in <unicode> and convert to <utf-8>
            perms = [x.encode('UTF8') for x in request.POST.getlist('checks')]
            # create empty list and append in it the <permissions objects>
            perms_list = []
            for perm in perms :
                perms_list += Permission.objects.filter(codename__contains=str(perm))
            # set perms_list into the user
            user.user_permissions.set(perms_list)
            user.save()
            return redirect(reverse('users:profile', kwargs= {"pk" :pk }))
        else:
            context = {
                "all_permissions" : allPermList,
                "user_permissions" : userPermList,
            }
            return render(request ,"users/edit-permissions.html" , context)
    else :
        return redirect(reverse('users:profile', kwargs= {"pk" :request.user.id }))

"""
who have permissions to add new user
and assign that user to the organization < slug = slug >
"""
@permission_required("users.can_add_organization_user")
def createOrganizationUser(request , slug):
    organization = Organization.objects.get(slug = slug)
    print(organization)
    if request.method == 'POST':
        form = OrganizationUserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.organization = organization
            instance.save()
            return redirect(reverse('organizations:organizations-list'))

    else :
        form = OrganizationUserCreateForm()
    context = {
    "form" : form,
    }
    return render(request, "create.html", context)
