# Generated by Django 3.2 on 2021-10-26 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20211026_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='website',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
