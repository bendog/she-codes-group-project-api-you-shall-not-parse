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




class MentorProcess(models.Model):
    mentor_name = models.ForeignKey(
        CustomUser, related_name="process", on_delete=models.CASCADE
    )
    sign_up = models.BooleanField(default=False)
    confirmation = models.BooleanField(default=False)
    send_contract = models.BooleanField(default=False)
    received_contract = models.BooleanField(default=False)
    calendar_invites = models.BooleanField(default=False)
    onboarding = models.BooleanField(default=False)
    mentoring = models.BooleanField(default=False)
    invoice_sent = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)


# @receiver(post_save, sender=MentorProfile)
# def create_related_process(sender, instance, created, *args, **kwargs):
#     if instance and created:
#         MentorProcess.objects.create(mentor_name=instance)