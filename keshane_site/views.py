import base64
from django.shortcuts import render
from django.core.mail import send_mail
from django.core.signing import Signer, BadSignature

from keshane_site import utils
from .models import Post
from .models import Tag
from .models import Subscriber
from .forms import SubscriberForm
from .forms import UnsubscribeForm


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
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "keshane_site/subscribe_success.html", request.POST, status=201)
        else:
            return render(request, "keshane_site/subscribe.html", {"subscribe_form":form})

    else:
        subscribe_form = SubscriberForm()
        return render(request, "keshane_site/subscribe.html", {"subscribe_form": subscribe_form})


def blog_unsubscribe_request(request):
    """Renders a form to allow subscribers to unsubscribe from the blog"""
    if request.method == "POST":
        form = UnsubscribeForm(request.POST)
        error_message = ""
        status = 400
        if form.is_valid():
            subscriber_email = form.cleaned_data["email_address"]
            try:
                Subscriber.objects.get(email_address=subscriber_email)
                unsubscribe_link = utils.generate_unsubscribe_link(subscriber_email)
                unsubscribe_email_message = "Please navigate to the following link to unsubscribe:\r\n" + unsubscribe_link
                send_mail("Link to unsubscribe from Keshane's blog", unsubscribe_email_message, "blog@keshane.com",
                          recipient_list=[subscriber_email])
                message = "An email has been sent to " + subscriber_email + " with a link to unsubscribe from my blog."
                return render(request, "keshane_site/unsubscribe_result.html", {"message": message})
            except Subscriber.DoesNotExist:
                error_message = "Sorry, that email was not found in the subscriber list."
                status = 404

        # else if form is not valid, return with error messages
        return render(request, "keshane_site/unsubscribe_request.html",
                      {"unsubscribe_form": form, "error_message": error_message}, status=status)
    else:
        form = UnsubscribeForm()
        return render(request, "keshane_site/unsubscribe_request.html", {"unsubscribe_form": form})


def blog_unsubscribe(request, unsubscribe_token):
    """Unsubscribes a subscriber if requested with a valid token"""
    status = 200
    padded_token = unsubscribe_token + ("=" * (4 - len(unsubscribe_token) % 4))
    token_bytes = padded_token.encode("UTF-8")
    decoded = base64.b64decode(token_bytes)
    signer = Signer(salt="unsubscribe")
    subscriber_email = ""
    try:
        subscriber_email = signer.unsign(decoded.decode("UTF-8"))
        Subscriber.objects.get(email_address=subscriber_email).delete()
        message = subscriber_email + " has been unsubscribed from Keshane's Blog."
    except Subscriber.DoesNotExist:
        message = subscriber_email + " is already unsubscribed. No action is needed."
        status = 404
    except BadSignature:
        message = "Sorry, this URL is not recognized."
        status = 404
    except UnicodeDecodeError:
        message = "Sorry, this URL is not recognized."
        status = 404
    return render(request, "keshane_site/unsubscribe_result.html", {"message": message}, status=status)
