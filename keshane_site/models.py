from django.core.mail import send_mass_mail
from django.urls import reverse
from django.db import models


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
    def notify_subscribers(self):
        """Lets readers subscribed to the blog about a change"""
        subject = "New post on Keshane's blog about " + self.title
        message = "Check out Keshane's insights at https://keshane.com" + reverse("blog") + "!"

        emails = tuple(
            (subject,
             "Dear " + subscriber.first_name + ",\r\n" + message,
             "blog@keshane.com",
             [subscriber.email_address])
            for subscriber in Subscriber.objects.all())

        send_mass_mail(emails)

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    """Defines the attributes of a viewer who is subscribed to the blog"""
    first_name = models.CharField(max_length=255)
    email_address = models.EmailField()

    def __str__(self):
        return self.first_name
