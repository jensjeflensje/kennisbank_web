from django.db import models

from user_auth.models import DiscordUser


class Guild(models.Model):
    discord_id = models.IntegerField()

    def __str__(self):
        return self.discord_id


class GuildChannel(models.Model):
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE)
    channel_id = models.IntegerField()

    def __str__(self):
        return f"{self.guild.discord_id} -> {self.channel_id}"


class Question(models.Model):
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    keywords = models.TextField()

    def __str__(self):
        return self.question

    def serialize(self):
        data = {
            "question": self.question,
            "answer": self.answer,
        }
        return data
