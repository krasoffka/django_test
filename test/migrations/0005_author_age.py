# Generated by Django 2.2.7 on 2019-11-22 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0004_auto_20191121_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='age',
            field=models.IntegerField(default=40),
            preserve_default=False,
        ),
    ]
