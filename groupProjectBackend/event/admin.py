from django.contrib import admin

from .models import Event, EventModule, EventModuleRole, Module, Role

# Register your models here.

admin.site.register(Role)
admin.site.register(Module)
admin.site.register(EventModule)


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


class EventModuleInline(admin.TabularInline):
   model = EventModule
   fields = ('module', 'start_time', 'end_time')
#    readonly_fields = ('added_date',)
   extra = 1


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
   inlines = (EventModuleInline,)