# Generated by Django 3.0.5 on 2020-04-18 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group_control', '0004_schedule_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
