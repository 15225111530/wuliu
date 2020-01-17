# Generated by Django 2.2.4 on 2020-01-17 13:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groupuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=10, verbose_name='用户组')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('creat_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '用户组',
                'verbose_name_plural': '用户组',
                'db_table': 'user_groups',
            },
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_account', models.CharField(max_length=10, verbose_name='账号')),
                ('username', models.CharField(max_length=10, verbose_name='用户名称')),
                ('password', models.CharField(max_length=10, verbose_name='用户密码')),
                ('token', models.CharField(max_length=255, verbose_name='token信息')),
                ('info', models.CharField(max_length=100, verbose_name='描述')),
                ('u_phone', models.CharField(max_length=30, verbose_name='用户手机')),
                ('ip', models.CharField(max_length=50, verbose_name='ip')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('creat_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_status', models.CharField(max_length=50, verbose_name='用户使用状态')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Userinfo.Groupuser')),
            ],
            options={
                'verbose_name': '账户信息表',
                'verbose_name_plural': '账户信息表',
                'db_table': 'user_userinfo',
                'unique_together': {('user_account', 'u_phone')},
            },
        ),
    ]
