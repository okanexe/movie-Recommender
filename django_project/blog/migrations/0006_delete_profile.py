# Generated by Django 3.0.7 on 2020-06-28 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_delete_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
