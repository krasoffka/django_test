# Generated by Django 2.2.7 on 2019-11-07 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('family', models.CharField(max_length=64)),
                ('patronymic', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=128)),
                ('unit', models.CharField(max_length=128)),
                ('organisation', models.CharField(max_length=128)),
                ('internal_phone', models.CharField(max_length=64)),
                ('official_phone', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=64)),
                ('birthday', models.DateField()),
                ('city', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=256)),
            ],
        ),
    ]
