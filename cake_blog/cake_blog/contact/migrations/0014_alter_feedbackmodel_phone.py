# Generated by Django 3.2 on 2021-11-03 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0013_alter_feedbackmodel_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackmodel',
            name='phone',
            field=models.CharField(max_length=12, verbose_name='Телефон'),
        ),
    ]
