from django.contrib import admin
from django.db import models


from .models import CustomUser




# @admin.register(CustomUser)

class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "location",
        "languages",
    )
    list_filter = (
        
        "location",
    )

    fields = ['username',('first_name','last_name'), ('email', 'contact'), 'image', 'bio', 'location', 'current_position', 'languages']


admin.site.register(CustomUser, UserAdmin)
