from rest_framework.routers import DefaultRouter

from member.views import (
    UserProfileViewSet,
)

user_router = DefaultRouter()

user_router.register(r'profile', UserProfileViewSet)
