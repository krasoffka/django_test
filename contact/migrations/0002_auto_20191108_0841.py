# Generated by Django 2.2.7 on 2019-11-08 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='family',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='contact',
            name='patronymic',
            field=models.CharField(max_length=128),
        ),
    ]
