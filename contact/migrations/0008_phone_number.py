# Generated by Django 2.2.7 on 2019-11-11 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_auto_20191111_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='number',
            field=models.CharField(default=123, max_length=64),
            preserve_default=False,
        ),
    ]