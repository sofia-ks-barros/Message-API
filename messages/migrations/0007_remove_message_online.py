# Generated by Django 5.1.6 on 2025-03-16 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0006_message_online'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='online',
        ),
    ]
