# Generated by Django 2.2.7 on 2019-11-12 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='contact.Contact'),
        ),
    ]
