# Generated by Django 4.0.3 on 2022-03-19 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_user_delete_posts_delete_users_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='1234', max_length=30),
        ),
    ]
