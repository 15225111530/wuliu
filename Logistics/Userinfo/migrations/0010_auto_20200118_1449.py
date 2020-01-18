# Generated by Django 2.2.4 on 2020-01-18 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userinfo', '0009_tlogcost'),
    ]

    operations = [
        migrations.AddField(
            model_name='theorder',
            name='the_party1_address',
            field=models.CharField(default=1, max_length=30, verbose_name='运输方1地址'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theorder',
            name='the_party1_phone',
            field=models.CharField(default=1, max_length=30, verbose_name='运输方1电话'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theorder',
            name='the_party2_address',
            field=models.CharField(default=1, max_length=30, verbose_name='运输方2地址'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theorder',
            name='the_party2_phone',
            field=models.CharField(default=1, max_length=30, verbose_name='运输方2电话'),
            preserve_default=False,
        ),
    ]
