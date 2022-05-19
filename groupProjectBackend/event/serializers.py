from rest_framework import serializers
from .models import Event, Role, Module, EventModule, EventModuleRole
from django.contrib.auth import get_user_model


class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ('name', 'description', 'published', 'signup_opens', 'signup_closes', 'location')


class RoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Role
        fields = ('name', 'capable_mentors')


class ModuleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Module
        fields = ('name', 'required_roles')


class EventModuleSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = EventModule
        fields = ('event', 'module', 'start_time', 'end_time')


class EventModuleRoleSerializer (serializers.ModelSerializer):
    mentor = serializers.ReadOnlyField(source="user.username")
    #these 2 fields disappeared from selection - they need to be there but cannot be changed
    class Meta:
        model = EventModuleRole
        fields = ('event_module', 'role', 'mentor', 'gift_back')