# Generated by Django 2.2.13 on 2020-06-14 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0003_auto_20200614_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areacode_m', models.CharField(max_length=6, verbose_name='エリアコード')),
                ('name', models.CharField(max_length=10, verbose_name='エリア名')),
            ],
        ),
        migrations.DeleteModel(
            name='Pref',
        ),
    ]
