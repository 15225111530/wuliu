# Generated by Django 2.2.4 on 2020-01-20 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userinfo', '0012_auto_20200120_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='theorder',
            name='freight1',
            field=models.CharField(default=1, max_length=30, verbose_name='运费'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theorder',
            name='freight2',
            field=models.CharField(default=1, max_length=30, verbose_name='运费'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theorder',
            name='goods_note1',
            field=models.CharField(default=1, max_length=30, verbose_name='货物备注'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theorder',
            name='goods_note2',
            field=models.CharField(default=1, max_length=30, verbose_name='货物备注'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theorder',
            name='packaging',
            field=models.CharField(default=1, max_length=20, verbose_name='包装'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theorder',
            name='packaging1',
            field=models.CharField(default=1, max_length=20, verbose_name='包装'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theorder',
            name='packaging2',
            field=models.CharField(default=1, max_length=20, verbose_name='包装'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theorder',
            name='rebates1',
            field=models.CharField(default=1, max_length=30, verbose_name='返款'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theorder',
            name='rebates2',
            field=models.CharField(default=1, max_length=30, verbose_name='返款'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theorder',
            name='single_price1',
            field=models.CharField(default=1, max_length=30, verbose_name='单价'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theorder',
            name='single_price2',
            field=models.CharField(default=1, max_length=30, verbose_name='单价'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theorder',
            name='transfer_fee',
            field=models.CharField(default=1, max_length=20, verbose_name='中转费'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theorder',
            name='transfer_fee1',
            field=models.CharField(default=1, max_length=20, verbose_name='中转费'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theorder',
            name='transfer_fee2',
            field=models.CharField(default=1, max_length=20, verbose_name='中转费'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='theorder',
            name='com_name1',
            field=models.CharField(max_length=30, verbose_name='货物名称1'),
        ),
        migrations.AlterField(
            model_name='theorder',
            name='com_name2',
            field=models.CharField(max_length=30, verbose_name='货物名称2'),
        ),
        migrations.AlterField(
            model_name='theorder',
            name='com_number1',
            field=models.CharField(max_length=30, verbose_name='货物数量1'),
        ),
        migrations.AlterField(
            model_name='theorder',
            name='com_number2',
            field=models.CharField(max_length=30, verbose_name='货物数量2'),
        ),
        migrations.AlterField(
            model_name='theorder',
            name='com_weight1',
            field=models.CharField(max_length=30, verbose_name='货物重量1'),
        ),
        migrations.AlterField(
            model_name='theorder',
            name='com_weight2',
            field=models.CharField(max_length=30, verbose_name='货物重量2'),
        ),
        migrations.AlterField(
            model_name='theorder',
            name='single_price',
            field=models.CharField(max_length=30, verbose_name='单价'),
        ),
    ]
