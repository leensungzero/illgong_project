from django.db import models
from django.contrib.auth import get_user_model

from utils.models import TimestampedModel


User = get_user_model()


class FriendRequest(TimestampedModel):
    request_user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='request_user',
        verbose_name='요청자',
    )

    response_user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='response_user',
        verbose_name='수락자',
    )

    assent = models.BooleanField(
        null=False,
        default=False,
        verbose_name='수락여부'
    )

    def __str__(self):
        return "{} -> {}" .format(self.request_user, self.response_user)
