from django.db import models
from django.contrib.auth import get_user_model

from utils.models import TimestampedModel


User = get_user_model()


class UserProfile(TimestampedModel):
    KOREAN = 'Korean'
    ENGLISH = 'English'

    LANGUAGE_CHOICES = (
        (KOREAN, 'KR'),
        (ENGLISH, 'EN'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, unique=True)
    birth = models.DateField()
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default="Korean")
    friends = models.ManyToManyField(User, related_name='friends')
