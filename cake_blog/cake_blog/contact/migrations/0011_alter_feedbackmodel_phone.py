# Generated by Django 3.2 on 2021-11-03 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_alter_feedbackmodel_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackmodel',
            name='phone',
            field=models.PositiveIntegerField(default=0, verbose_name='Телефон'),
        ),
    ]
