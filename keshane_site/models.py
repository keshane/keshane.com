from django.core.mail import send_mass_mail
from django.urls import reverse
from django.db import models
from keshane_com import settings
from keshane_site import utils


class Tag(models.Model):
    """Defines a tag, i.e. a keyword associated with a blog post"""
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Post(models.Model):
    """Defines the contents of a blog post"""
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        """Adds custom behavior to notify subscribers when a post has been created"""
        if self._state.adding:
            self.notify_subscribers()
        super().save(*args, **kwargs)

    # TODO put messages in database
    # TODO put this method in a view?
    def notify_subscribers(self):
        """Lets readers subscribed to the blog know about a change"""

        subject = "New post on Keshane's blog about " + self.title

        emails = tuple(
            (subject,
             Post.create_subscriber_notification_email(subscriber),
             "Keshane's Blog <blog@keshane.com>",
             [subscriber.email_address])
            for subscriber in Subscriber.objects.all())

        send_mass_mail(emails)

    @staticmethod
    def create_subscriber_notification_email(subscriber):
        """Composes the email to send subscribers about a new blog post"""
        message_content = "Check out Keshane's newest insights at " + settings.DOMAIN + reverse("blog") + " !"
        footer = "If you would like to unsubscribe, navigate to the following link: "\
                 + utils.generate_unsubscribe_link(subscriber.email_address)
        message = "Dear {name},\r\n{message_content}\r\n\r\n{footer}".format(name=subscriber.first_name,
                                                                             message_content=message_content,
                                                                             footer=footer)
        return message

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    """Defines the attributes of a viewer who is subscribed to the blog"""
    first_name = models.CharField(max_length=255)
    email_address = models.EmailField(unique=True)

    def __str__(self):
        return self.first_name
