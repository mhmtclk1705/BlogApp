from multiprocessing import context
from django.shortcuts import render,redirect

# Create your views here.
from .forms import PostForm, CommentForm
from .models import Post, Comment,PostView,Like
from django.views import generic
from django.contrib import messages
def post_create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            # if 'image' in request.FILES:
            #     post.image = request.FILES['image']
            post.save()
            messages.success(request, 'Post Created')
            return redirect('post_list')
    return render(request, 'blog/post_create.html', {'form': form})

def post_list(request):
    posts = Post.objects.all()

    return render(request, 'blog/post_list.html', {'posts': posts})

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    # post.views = post.views + 1
    post.comments = Comment.objects.filter(post=post)
    post.save()
    if request.user.is_authenticated:
        PostView.objects.create(user=request.user, post=post)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})

def post_update(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post Updated')
            return redirect('post_detail', slug=slug)
    return render(request, 'blog/post_update.html', {'form': form})

def post_delete(request, slug):
    post = Post.objects.get(slug=slug)
    post.delete()
    messages.success(request, 'Post Deleted')
    return redirect('post_list')

def post_like(request, slug):
    post = Post.objects.get(slug=slug)
    like = Like.objects.filter(user=request.user, post=post)
    if like.exists():
        like[0].delete()
    else:
        Like.objects.create(user=request.user, post=post)
    return redirect('post_detail', slug=slug)
