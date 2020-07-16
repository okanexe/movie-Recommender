# Generated by Django 3.0.7 on 2020-06-29 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='movies',
            name='IMDBScore',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
