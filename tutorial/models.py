from django.contrib.auth.models import User
from django.db import models
import uuid

from user.models import UserProfile


class Image(models.Model):
    """ image model"""
    title = models.CharField(max_length=200, null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.title)


class Video(models.Model):
    """ Video model"""
    title = models.CharField(max_length=200, null=True, blank=True)
    video_url = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.title)


class Keyword(models.Model):
    """keyword model"""
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class ContentType(models.Model):
    """ContentType model"""
    content = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.content


class Tutorial(models.Model):
    """ admin/user can create tutorial"""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='author', null=True, blank=True)
    publish_date = models.DateField(auto_now_add=True)
    comments = models.TextField(null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='content_types', null=True,
                                     blank=True)
    keywords = models.ManyToManyField(Keyword,  related_name='keywords')
    images = models.ManyToManyField(Image,  related_name='images')
    videos = models.ManyToManyField(Video,  related_name='videos')

    def __str__(self):
        return str(self.title)
