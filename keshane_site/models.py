from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

