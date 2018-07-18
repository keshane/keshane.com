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

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    """Defines the attributes of a viewer who is subscribed to the blog"""
    first_name = models.CharField(max_length=255)
    email_address = models.EmailField()

    def __str__(self):
        return self.first_name