# Generated by Django 2.2.7 on 2019-11-18 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0002_auto_20191118_1518'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['friends__id']},
        ),
        migrations.AlterField(
            model_name='author',
            name='friends',
            field=models.ManyToManyField(null=True, to='test.Author'),
        ),
    ]
