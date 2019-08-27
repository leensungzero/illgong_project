from django.contrib.auth import password_validation
from django.contrib.auth import get_user_model
from rest_framework import serializers

from member.models.user_profile import UserProfile


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
        )

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save(update_fields=['password'])

        return user

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)

        return value


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer()
    birth = serializers.DateField(write_only=True)
    friends = UserSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = (
            'id',
            'user',
            'username',
            'nickname',
            'birth',
            'language',
            'friends',
        )

    def create(self, validated_data):
        validated_data['user'] = UserSerializer.create(UserSerializer(), validated_data=validated_data['user'])
        user_profile = super().create(validated_data)

        return user_profile
