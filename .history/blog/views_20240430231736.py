from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.http import Http404

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts' : posts})


def post_detail(request,year, month, day, post):

    post = get_object_or_404(Post,id=id,status=Post.Status.PUBLISHED, year=year, month=month, day=)
    
    return render(request,'blog/post/detail.html',{'post' : post})