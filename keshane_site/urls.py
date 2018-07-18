from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("blog/", views.blog, name="blog"),
    path("blog/tags/", views.blog_all_tags, name="blog_all_tags"),
    path("blog/tags/<str:tag>/", views.blog_tag, name="blog_tag"),
    path("blog/subscribe/", views.blog_subscribe, name="blog_subscribe"),
]
