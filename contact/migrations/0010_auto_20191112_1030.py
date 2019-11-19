# Generated by Django 2.2.7 on 2019-11-12 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_auto_20191112_0805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='contact',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contact.Department'),
        ),
        migrations.AddField(
            model_name='contact',
            name='subdivision',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contact.Subdivision'),
        ),
    ]