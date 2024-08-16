from rest_framework import serializers

from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(username=validated_data['username'],
                                              password=validated_data['password'],
                                              email=validated_data['email'])
        return user
