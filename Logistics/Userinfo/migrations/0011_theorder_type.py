# Generated by Django 2.2.4 on 2020-01-20 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userinfo', '0010_auto_20200118_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='theorder',
            name='type',
            field=models.CharField(default=1, max_length=30, verbose_name='货物类型'),
            preserve_default=False,
        ),
    ]
