from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog, name="blog"),
    path("tags/", views.all_tags, name="all_tags"),
    path("tags/<str:tag>/", views.tag, name="tag"),
    path("subscribe/", views.subscribe, name="subscribe"),
    path("unsubscribe/", views.unsubscribe, name="unsubscribe"),
    path("unsubscribe/<str:unsubscribe_token>", views.unsubscribe_user, name="unsubscribe_user"),
]