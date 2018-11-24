# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from posts.models import Post

def home(request):
    posts       = Post.objects.all()
    context = {
    "posts" : posts,
    }
    return render(request, "home.html", context)
