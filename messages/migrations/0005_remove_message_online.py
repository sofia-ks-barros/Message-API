# Generated by Django 5.1.6 on 2025-03-09 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_message_online'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='online',
        ),
    ]
