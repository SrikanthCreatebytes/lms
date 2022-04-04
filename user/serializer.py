from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import UserProfile, User


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField()

    class Meta:
        model = UserProfile
        fields = ['email', ]


class CRUDUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

    def create(self, validated_data):
        user_obj = User.objects.create(username=validated_data.get('first_name'), email=validated_data.get('email'),
                                       is_superuser=validated_data.get('is_admin'),
                                       password=validated_data.get('password'))
        return UserProfile.objects.create(user=user_obj, **validated_data)
