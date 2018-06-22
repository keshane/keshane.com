from django.shortcuts import render
from keshane_site.models import Post


def index(request):
    """Renders the home (index) page of the site"""
    return render(request, 'keshane_site/index.html')


def contact(request):
    """Renders the contact page"""
    return render(request, 'keshane_site/contact.html')


def blog(request):
    """Retrieves blogs from the database and renders them"""
    # TODO

    posts = Post.objects.order_by("date_added")
    data = {"posts": posts}
    return render(request, 'keshane_site/blog.html', data)