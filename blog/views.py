from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Post

class HomePageView(ListView):
    model = Post
    context_object_name = "all_post"
    template_name = "home.html"
