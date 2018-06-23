from django.shortcuts import render
from keshane_site.models import Post
from keshane_site.models import Tag


def index(request):
    """Renders the home (index) page of the site"""
    return render(request, 'keshane_site/index.html')


def contact(request):
    """Renders the contact page"""
    return render(request, 'keshane_site/contact.html')


def blog(request):
    """Retrieves blogs from the database and renders them"""
    posts = Post.objects.order_by("-date_added")
    data = {"posts": posts}
    return render(request, 'keshane_site/blog.html', data)


def blog_tag(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    data = {"posts": posts}
    return render(request, 'keshane_site/blog.html', data)


def blog_all_tags(request):
    tags = Tag.objects.all()
    data = {"tags": tags}
    return render(request, 'keshane_site/tags.html', data)
