# Generated by Django 2.2.13 on 2020-06-14 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0004_auto_20200614_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='areacode_m',
            field=models.CharField(max_length=10, verbose_name='エリアコード'),
        ),
    ]