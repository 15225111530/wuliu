# Generated by Django 2.2.4 on 2020-02-16 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userinfo', '0014_theorder_all_freight'),
    ]

    operations = [
        migrations.AddField(
            model_name='tlogcost',
            name='address',
            field=models.CharField(default=1, max_length=30, verbose_name='地址'),
            preserve_default=False,
        ),
    ]
