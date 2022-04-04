from django.contrib import admin
from .models import Image, Video, ContentType, Tutorial, Keyword, Tutorial

admin.site.register(Image)
admin.site.register(Video)
admin.site.register(ContentType)
admin.site.register(Keyword)
admin.site.register(Tutorial)
