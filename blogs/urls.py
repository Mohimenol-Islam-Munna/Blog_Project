from django.urls import path
from .views import BlogPostView, BlogDetailView, AddNewBlogPost, EditBlogPost

urlpatterns = [
    path("post/edit/<int:pk>", EditBlogPost.as_view(), name="edit_post"),
    path("post/new", AddNewBlogPost.as_view(), name="new_post"),
    path("post/<int:pk>", BlogDetailView.as_view(), name="post_details"),
    path("", BlogPostView.as_view(), name="blog_post"),
]
