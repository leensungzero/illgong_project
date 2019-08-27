from django.db import models
from django.contrib.auth.models import AbstractUser

from member.models.user_manager import UserManager


class User(AbstractUser):
    username = None
    nickname = None
    email = models.EmailField(
        unique=True,
        verbose_name='이메일',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'User(ID {self.id})'

    class Meta:
        db_table = 'user'
        verbose_name = '유저'
        verbose_name_plural = '{} {}'.format(verbose_name, '목록')
