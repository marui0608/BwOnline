# Generated by Django 2.2.5 on 2020-05-14 10:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation', '0002_auto_20200513_2318'),
    ]

    operations = [
        # migrations.AddField(
            # model_name='usercourse',
            # name='course',
            # field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='课程'),
            # preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='userfavorite',
        #     name='user',
        #     field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        #     preserve_default=False,
        # ),
        migrations.AlterField(
            model_name='coursecomments',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='coursecomments',
            name='comments',
            field=models.CharField(max_length=200, verbose_name='评论'),
        ),
        migrations.AlterField(
            model_name='userfavorite',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userfavorite',
            name='fav_id',
            field=models.IntegerField(default=0, verbose_name='数据id'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='user',
            field=models.IntegerField(default=0, verbose_name='接受用户'),
        ),
    ]