from django.db import models
from django.contrib.auth import get_user_model

from utils.models import TimestampedModel


User = get_user_model()


class Schedule(TimestampedModel):
    registrant = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        related_name='registrant',
        verbose_name='등록자',
    )
    participants = models.ManyToManyField(
        to=User,
        related_name='participants',
        verbose_name='참가자들',
    )
    title = models.CharField(
        max_length=300,
        verbose_name='제목',
    )
    state = models.IntegerField(
        default=0,
        verbose_name='상태',
    )
    start_time = models.DateTimeField()
    latitude = models.FloatField(
        null=True,
        blank=True,
        verbose_name='위도',
    )
    longitude = models.FloatField(
        null=True,
        blank=True,
        verbose_name='경도',
    )
    contents = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name='내용',
    )

    def __str__(self):
        return f'Schedule(ID {self.id}, by {self.registrant}, at {self.created_datetime})'

    class Meta:
        db_table = 'schedule'
        verbose_name = '일정'
        verbose_name_plural = '{} {}'.format(verbose_name, '목록')
