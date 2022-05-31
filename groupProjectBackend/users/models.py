from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    image = models.URLField(null=True)
    current_position = models.CharField(max_length=100, null=True)
    bio = models.TextField(null=True)
    contact = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    languages = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.username





# @receiver(post_save, sender=MentorProfile)
# def create_related_process(sender, instance, created, *args, **kwargs):
#     if instance and created:
#         MentorProcess.objects.create(mentor_name=instance)