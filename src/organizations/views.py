# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import OrganizationUserCreateForm, OrganizationCreateForm, OrganizationUpdateForm
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from users.models import CustomUser
from .models import Organization
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.decorators import permission_required, user_passes_test

"""
# user who don't belong to any organizations only who can create a new organization
# assign the organization to the owner user
# set is_owner value to True
"""
def organizationsCreate(request):
    if request.user.organization == None :
        user_id = request.user.id
        user = CustomUser.objects.get(id = user_id)
        if request.method == "POST":
            form = OrganizationCreateForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.owner_id = int(request.user.id)
                instance.save()
                all_permissions =  Permission.objects.filter(codename__contains="organization")
                print(all_permissions)
                user.user_permissions.set(all_permissions)
                user.organization = instance
                user.is_owner = True
                user.save()
                return redirect(reverse('home'))
                # return redirect(reverse('organizations:myorganizations-list'))
        else :
            form = OrganizationCreateForm()
        context = {
        "form" : form ,
        }
        return render(request, "create.html",context)
    else:
        return HttpResponse("<script>alert('You can not add new Organization Because you are a member in {} organization');</script>".format(request.user.organization))

"""
My Organization
# not very important because user have only one organization so
# it can show the detail view directly
"""
def myOrganizationsList(request):
    user_organization = request.user.organization
    user_role = ''
    if user_organization :
        if user_organization.owner_id == request.user.id:
            user_role = 'You are The Owner Of that Organization'
        else :
            user_role = 'You are a Member of that Organization '

    context = {
    "organization" : user_organization,
    "user_role" :user_role
    }
    return render(request, "organizations/organizations-list.html", context)

"""
show all organizations for the staff users "is_satff or is_superuser"
"""
def isStaff(user):
    return True if user.is_staff or user.is_superuser else False

@user_passes_test(isStaff , login_url = 'users:login')
def organizationsList(request):
    organizations = Organization.objects.all()
    context = {
    "organizations" : organizations,
    }
    return render(request, "organizations/admin-organizations-list.html", context)

"""
show organization details
"""
def organizationDetail(request, slug):
    organization        = Organization.objects.get(slug= slug)
    user_id             = organization.owner_id
    user                = CustomUser.objects.get(id = user_id)
    organization_users  = organization.users.all()
    user_role = ''
    if request.user.organization != None :
        if request.user.organization.owner_id == request.user.id :
            user_role = 'You are The Owner Of that Organization'
        else :
            user_role = 'You are a Member of that Page '
    context      = {
    "user"               : user,
    "organization_users" : organization_users,
    "organization"       : organization,
    "user_role"          : user_role,
    }
    return render(request, "organizations/organizations-detail.html", context)

"""
update the organiztion
"""
class OrganizationsUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    permission_required = 'users.change_organization'
    form_class = OrganizationUpdateForm
    template_name = "create.html"
    queryset = Organization.objects.all()
