from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password




class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'image', 'current_position', 'bio', 'location', 'contact', 'languages')

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)



class CustomUserDetailSerializer(CustomUserSerializer):
    
    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.current_position = validated_data.get('current_position', instance.current_position)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.location=validated_data.get('location', instance.location)
        instance.contact=validated_data.get('contact', instance.contact)
        instance.languages=validated_data.get('languages', instance.languages)
        instance.save()
        return instance





class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'bio', 'current_position', 'image', 'location', 'contact', 'languages')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            bio=validated_data['bio'],
            image=validated_data['image'],
            current_position=validated_data['current_position'],
            location=validated_data['location'],
            contact=validated_data['contact'],
            languages=validated_data['languages'],
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user