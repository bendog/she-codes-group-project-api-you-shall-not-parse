from django.contrib import admin
import django.apps

from .models import Event, EventModule, EventModuleRole, Module, Role

# Register your models here.

admin.site.register(Role)
admin.site.register(Module)
admin.site.register(EventModule)
# admin.site.register(EventModuleRole)


@admin.register(EventModuleRole)
class EventModuleRoleAdmin(admin.ModelAdmin):
    list_display = (
        "event_module",
        "role",
        "mentor",
        "gift_back",
    )
    list_filter = (
        "gift_back",
        ("mentor", admin.EmptyFieldListFilter),
    )
    
    
    fieldsets =(
        ("Event",{
            "fields": ("event","event_module", "role", "mentor", "gift_back")
        }),
        ("Mentor Onboarding Process", {
            "fields": ("sign_up", "confirmation", "send_contract", "received_contract", "calendar_invites", "onboarding", "mentoring", "invoice_sent", "paid")
        }),
    )
    


class EventModuleInline(admin.TabularInline):
    model = EventModule
    fields = ('module', 'start_time', 'end_time')
#    readonly_fields = ('added_date',)
    extra = 1


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = (EventModuleInline,)


# models = django.apps.apps.get_models()
# print(models)

# admin.site.unregister(django.contrib.auth.models.Group)

