# Generated by Django 2.2.12 on 2021-03-03 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinformationforms',
            name='address',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='personalinformationforms',
            name='contactnumber',
            field=models.CharField(max_length=15),
        ),
    ]