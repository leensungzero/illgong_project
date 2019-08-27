from django.urls import path

from member.views import email_validate


urlpatterns = [
    path('validate/email/', email_validate, name='email_validate'),
]
