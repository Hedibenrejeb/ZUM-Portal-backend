# Generated by Django 4.0.5 on 2022-12-15 14:30

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='users/default.png', upload_to=authentication.models.upload_path, verbose_name='photo'),
        ),
    ]
