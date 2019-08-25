from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    email = models.EmailField(
        unique=True,
        verbose_name='이메일',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'User(ID {self.id})'

    class Meta:
        db_table = 'user'
        verbose_name = '유저'
        verbose_name_plural = '{} {}'.format(verbose_name, '목록')
