# Generated by Django 2.2.4 on 2020-01-17 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userinfo', '0007_auto_20200117_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='theorder',
            name='the_party1',
            field=models.CharField(default=1, max_length=30, verbose_name='运输方1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theorder',
            name='the_party2',
            field=models.CharField(default=1, max_length=30, verbose_name='运输方2'),
            preserve_default=False,
        ),
    ]
