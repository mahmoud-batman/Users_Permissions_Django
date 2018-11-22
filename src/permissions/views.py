# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import permission_required, user_passes_test
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from users.models import CustomUser
from django.urls import reverse


"""
only super user who can create new permission
"""
def isSuperuser(user):
    return True if user.is_superuser else False

@user_passes_test(isSuperuser , login_url = 'users:login')
def createPermissions(request, slug):
    if request.method == "POST":
        instance = request.POST
        code_name = instance["code_name"]
        name = instance["name"]
        # instance.save()
        ct = ContentType.objects.get_for_model(CustomUser) # @permission_required("users.can_view_organization_user")
        permission = Permission.objects.create(
        codename=str(code_name),
        name=str(name),
        content_type = ct
        )
        request.user.user_permissions.add(permission)
        return redirect(reverse("permissions:create-permissions" , kwargs= {"slug" :slug }))
    else:
        permissions= request.user.user_permissions.all()
    context = {
    "permissions" : permissions ,
    }
    return render(request, "permissions/create_permissions.html", context)

"""
only super user who can edit permission 
"""
@user_passes_test(isSuperuser , login_url = 'users:login')
def editPermissions(request, pk):
    if request.method == "POST":
        perm = Permission.objects.get(id= pk)
        perm.delete()
        instance = request.POST
        code_name = instance["code_name"]
        name = instance["name"]
        print(code_name, name)
        ct = ContentType.objects.get_for_model(CustomUser)
        permission = Permission.objects.create(
        codename=str(code_name),
        name=str(name),
        content_type = ct
        )
        request.user.user_permissions.add(permission)
        # return redirect(reverse("permissions:create-permissions" , kwargs= {"slug" :slug }))
        return redirect("/")
    perm = Permission.objects.get(id= pk)
    context= {
    "permission"  : perm
        }
    return render(request, "permissions/edit.html", context)
