from rest_framework import viewsets

from member.models.user_profile import UserProfile
from member.serializers import (
    UserProfileSerializer,
)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
