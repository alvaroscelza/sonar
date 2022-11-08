from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image_src = models.ImageField(upload_to='post', default='post/default_image.png')
    likes_amount = models.IntegerField(default=0)


class ActivityLog(models.Model):
    class InteractionTypes(models.TextChoices):
        LIKE = 'like', 'Like'
        VIEW = 'view', 'View'

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    interaction_type = models.CharField(choices=InteractionTypes.choices, max_length=4)
    timestamp = models.DateTimeField(auto_now_add=True)
