# Generated by Django 3.2.16 on 2022-11-12 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purria_backend', '0005_auto_20221112_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='gardens_count',
        ),
    ]
