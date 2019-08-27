from django.db import models
from django.contrib.auth import get_user_model

from utils.models import TimestampedModel


User = get_user_model()


class UserProfile(TimestampedModel):
    KOREAN = 'KR'
    ENGLISH = 'EN'

    LANGUAGE_CHOICES = (
        (KOREAN, 'Korean'),
        (ENGLISH, 'English'),
    )

    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='유저',
    )
    username = models.CharField(
        max_length=30,
        verbose_name='이름'
    )
    nickname = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='닉네임'
    )
    birth = models.DateField(
        verbose_name='생년월일'
    )
    language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES,
        default="Korean",
        verbose_name='언어'
    )
    friends = models.ManyToManyField(
        to=User,
        related_name='friends',
        verbose_name='친구목록',
    )

    def __str__(self):
        return f'UserProfile(ID {self.id}, by {self.user}, at {self.created_datetime})'

    class Meta:
        db_table = 'userProfile'
        verbose_name = '프로필'
        verbose_name_plural = '{} {}'.format(verbose_name, '목록')
