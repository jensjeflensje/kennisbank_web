from django.db import models
from django.contrib.auth.models import User


class DiscordUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField()
    userid = models.TextField()
    banned = models.BooleanField(default=False)

    def __str__(self):
        return self.name
