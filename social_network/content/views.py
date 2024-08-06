from django.http import (
    HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseNotAllowed
)
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

def posts_list(request):
    if request.method == "GET":
        # return HttpResponse(Post.objects.all())
        context = {"posts": Post.objects.all(), "form": PostForm()}
        return render(request, "content/posts.html", context)
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            return HttpResponseRedirect(reverse("post_details", args=[new_post.id]))
        else:
            return HttpResponseBadRequest({"details": form.errors})
    else:
        return HttpResponseNotAllowed(["GET", "POST"])

def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post_details.html", {"post": post})

def index(request):
    return render(request, "index.html", {})

def hello(request, username):
    return HttpResponse(f"Hello {username}!")

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.dislikes.all():
        post.dislikes.remove(request.user)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', post_id=post_id)

def dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    if request.user in post.dislikes.all():
        post.dislikes.remove(request.user)
    else:
        post.dislikes.add(request.user)
    return redirect('post_detail', post_id=post_id)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # или другая страница
    else:
        form = PostForm()
    return render(request, 'content/create_post.html', {'form': form})

def api_posts(request):
    result = list()
    for posts in Post.objects.all()
        result.appent{
            "id": posts.id,
            "title": posts.title
            "text": post.text
        }
    return HttpResponse()
def post_list(request):
    posts = Post.objects.all().order_by('-likes', 'dislikes')
    return render(request, 'content/post_list.html', {'posts': posts})