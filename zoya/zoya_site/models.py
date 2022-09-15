from django.db import models


class DiscordUser(models.Model):
    name = models.CharField(max_length=125)
    discord_id = models.IntegerField()

    def __str__(self):
        return self.name


class EXP (models.Model):
    user = models.OneToOneField(DiscordUser, on_delete=models.CASCADE)
    exp = models.IntegerField(default=0)
    lvl = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.name} EXP"


class Message (models.Model):
    name = models.CharField(max_length=125)
    text = models.TextField()

    def __str__(self):
        return f"{self.name} - wiadomość"
