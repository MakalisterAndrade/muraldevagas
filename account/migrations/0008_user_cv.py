# Generated by Django 3.2.16 on 2023-06-15 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cv',
            field=models.FileField(default=None, upload_to='resume/'),
        ),
    ]
