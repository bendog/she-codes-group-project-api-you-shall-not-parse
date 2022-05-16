from rest_framework import serializers

class EventSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=64)
    description = serializers.TextField()
    published = serializers.BooleanField(default=False)
    signup_opens = serializers.DateTimeField()
    signup_closes = serializers.DateTimeField()
    location = serializers.CharField(max_length=100)
