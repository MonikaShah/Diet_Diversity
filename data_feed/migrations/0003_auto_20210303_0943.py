# Generated by Django 2.2.12 on 2021-03-03 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_feed', '0002_auto_20210303_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyscheduleform',
            name='eatfrom',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='dailyscheduleform',
            name='eatto',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='dailyscheduleform',
            name='playfrom',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='dailyscheduleform',
            name='playto',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='dailyscheduleform',
            name='sleepfrom',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='dailyscheduleform',
            name='sleepto',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='dailyscheduleform',
            name='studyfrom',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='dailyscheduleform',
            name='studyto',
            field=models.TimeField(null=True),
        ),
    ]