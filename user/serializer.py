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
        user = validated_data.get('user')
        if user:
            user_obj = User.objects.get(id=user.id)
            return UserProfile.objects.create(user_id=user_obj.id, **validated_data)