# Generated by Django 4.2.3 on 2023-07-14 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_status_rocket_stage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rocket',
            name='build_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
