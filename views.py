from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# class PostList(ListView):
#     model = Post
#     ordering = '-pk'
#     paginate_by = 5
#
# class PostDetail(DetailView):
#     model = Post

def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(request,'post_list.html',
                  { 'posts':posts,})

def detailpost(request, pk):
    post = Post.objects.get(pk=pk)

    return render(request, 'post_detail.html',
                  { 'post':post})