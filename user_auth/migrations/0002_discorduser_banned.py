# Generated by Django 3.0.5 on 2020-04-29 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discorduser',
            name='banned',
            field=models.BooleanField(default=False),
        ),
    ]