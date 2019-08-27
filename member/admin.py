from django.contrib import admin
from django.contrib.auth import get_user_model

from member.models.user_profile import UserProfile


User = get_user_model()


admin.site.register(User)
admin.site.register(UserProfile)
