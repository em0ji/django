# Generated by Django 3.2 on 2021-10-23 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_authir_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
    ]
