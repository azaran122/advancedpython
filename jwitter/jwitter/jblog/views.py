from django.shortcuts import render
from django.http import HttpResponse
from jblog.models import Post
# Create your views here.


def index(request):
    # return HttpResponse("hi there")
    ret = '<body>'
    all_posts = Post.objects
    for post in all_posts:
        ret = ret+'<p>'+post.text + '<p>'
    ret = ret+'</body>'

    return HttpResponse(ret)
