# Generated by Django 2.2.7 on 2019-11-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='friends',
            field=models.ManyToManyField(to='test.Author'),
        ),
    ]