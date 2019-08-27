# Generated by Django 2.2.4 on 2019-08-26 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20190826_1158'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='language',
            field=models.CharField(choices=[('KR', 'Korean'), ('EN', 'English')], default='Korean', max_length=2, verbose_name='언어'),
        ),
    ]
