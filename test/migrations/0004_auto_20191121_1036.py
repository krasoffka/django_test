# Generated by Django 2.2.7 on 2019-11-21 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0003_auto_20191118_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='author',
            name='friends',
            field=models.ManyToManyField(blank=True, to='test.Author'),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.Author')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
