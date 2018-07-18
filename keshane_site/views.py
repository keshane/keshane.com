from django.http import HttpResponse
from django.shortcuts import render
from keshane_site.models import Post
from keshane_site.models import Tag
from keshane_site.forms import SubscriberForm


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
    """Retrieves blogs from the database with the specific tag and renders them"""
    posts = Post.objects.filter(tags__name=tag).order_by("-date_added")
    data = {"posts": posts}
    return render(request, 'keshane_site/blog.html', data)


def blog_all_tags(request):
    """Retrieves all tags from the database and renders them"""
    tags = Tag.objects.all()
    data = {"tags": tags}
    return render(request, 'keshane_site/tags.html', data)


def blog_subscribe(request):
    """Renders a form to allow viewers to subscribe to the blog"""
    if (request.method == "POST"):
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "keshane_site/subscribe_success.html", request.POST, status=201)

    else:
        subscribe_form = SubscriberForm()
        return render(request, "keshane_site/subscribe.html", {"subscribe_form": subscribe_form})
