# Generated by Django 4.0.5 on 2022-12-05 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='images/'),
        ),
    ]
