# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
import json
# Create your views here.
def addNewPost(request):
    if request.method == "POST" :
        title                    = request.POST["title"]
        body                     = request.POST["body"]
        print(title, body)
        post                     = Post.objects.create(title=title, body=body)
        post.save()
        print(post)
        response_data = {}
        response_data["title"]      = post.title
        response_data["body"]       = post.body
        response_data["updated_at"] = str(post.updated_at)
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

    else :
        return HttpResponse("Error.....")
