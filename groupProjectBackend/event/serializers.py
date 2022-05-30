from rest_framework import serializers

from users.models import CustomUser
from .models import Event, Role, Module, EventModule, EventModuleRole
from django.contrib.auth import get_user_model


class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'image', 'published', 'signup_opens', 'signup_closes', 'location')


class RoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Role
        fields = ('name', 'capable_mentors')


class ModuleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Module
        fields = ('name', 'required_roles')


class EventModuleSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    event = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Event.objects.all()
    )
    module = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Module.objects.all()
        )
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()


    def create(self, validated_data):
        return EventModule.objects.create(**validated_data)
    

#ORIGINAL SERIALIZER - NOT WORKING
# class EventModuleRoleSerializer (serializers.ModelSerializer):
#     id = serializers.ReadOnlyField()
#     event = serializers.ReadOnlyField(source="event.name")
#     event_module = serializers.ReadOnlyField(source="module.name")
#     # event_module = serializers.SlugRelatedField(
#     #     slug_field='module',
#     #     queryset=EventModule.objects.all()
#     #     )

#     role = serializers.SlugRelatedField(
#         slug_field='name',
#         queryset=Role.objects.all()
#     )
#     mentor = serializers.SlugRelatedField(
#         slug_field='username',
#         queryset=CustomUser.objects.all()
#     )

#     class Meta:
#         model = EventModuleRole
#         fields = ('id', 'event','event_module', 'role', 'mentor', 'gift_back')


#####ORIGINAL

# class EventModuleRoleSerializer (serializers.ModelSerializer):
#     # id = serializers.ReadOnlyField()
#     # event = serializers.ReadOnlyField(source="event.name")
#     # event_module = serializers.ReadOnlyField(source="module.name")
#     # event_module = serializers.SlugRelatedField(
#     #     slug_field='module',
#     #     queryset=EventModule.objects.all()
#     #     )

#     role = serializers.SlugRelatedField(
#         slug_field='name',
#         queryset=Role.objects.all()
#     )
#     mentor = serializers.SlugRelatedField(
#         slug_field='username',
#         queryset=CustomUser.objects.all()
#     )

#     class Meta:
#         model = EventModuleRole
#         fields = ('id','event_module', 'role', 'mentor', 'gift_back')


class EventModuleRoleSerializer (serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    event = serializers.ReadOnlyField(source="event.name")
    event_module_name = serializers.ReadOnlyField(source="event_module.module.name")

    role = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Role.objects.all()
    )
    mentor = serializers.SlugRelatedField(
        slug_field='username',
        queryset=CustomUser.objects.all()
    )

    class Meta:
        model = EventModuleRole
        fields = ('id', 'event', 'event_module_name', 'role', 'mentor', 'gift_back')