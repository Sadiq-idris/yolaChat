# Generated by Django 4.1.5 on 2023-05-13 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="message",
            old_name="data",
            new_name="date",
        ),
    ]
