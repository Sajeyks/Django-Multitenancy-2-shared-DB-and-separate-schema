# Generated by Django 4.2.3 on 2023-07-14 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_rocket_build_end'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='launch',
            name='reentry_time',
        ),
    ]
