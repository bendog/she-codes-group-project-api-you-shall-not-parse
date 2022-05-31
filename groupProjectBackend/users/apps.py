from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


# class MentorsAdminConfig(AdminConfig):
#     default_site = "blog.admin.BlogAdminArea"

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

