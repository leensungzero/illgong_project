from django.db import models

from utils.models import TimestampedModel


class Holiday(TimestampedModel):
    name = models.CharField(
        max_length=50,
        verbose_name='이름',
    )
    is_holiday = models.BooleanField(
        default=False,
        verbose_name='휴일여부',
    )
    date = models.DateField(
        verbose_name='날짜',
    )

    def __str__(self):
        return f'Holiday(ID {self.id}, at {self.created_datetime})'

    class Meta:
        db_table = 'holiday'
        verbose_name = '휴일'
        verbose_name_plural = '{} {}'.format(verbose_name, '목록')
