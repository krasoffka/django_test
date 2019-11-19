# Generated by Django 2.2.7 on 2019-11-11 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20191108_0841'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['id']},
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='family',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='unit',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='internal_phone',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='official_phone',
        ),
    ]