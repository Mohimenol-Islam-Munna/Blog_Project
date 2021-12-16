from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Post


class BlogPostView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class AddNewBlogPost(CreateView):
    model = Post
    template_name = "add_new_post.html"
    fields = ['title', 'author', 'body']


class EditBlogPost(UpdateView):
    model = Post
    template_name = "edit_post.html"
    fields = ['title', 'body']
