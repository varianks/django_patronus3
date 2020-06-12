from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Reference(models.Model):

    title = models.CharField(max_length = 250)
    description = models.CharField(max_length = 250)
    link = models.URLField(max_length=200)
    author = models.ForeignKey(User,
                                on_delete = models.CASCADE,
                                related_name = 'desc_posts' )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

