# Generated by Django 3.2 on 2021-10-26 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_about_imageabout_social'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='icon',
            field=models.FileField(upload_to='icons/'),
        ),
    ]
