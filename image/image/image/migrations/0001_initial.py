# Generated by Django 3.2.9 on 2021-11-06 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_text', models.CharField(max_length=200)),
                ('price_text', models.CharField(max_length=200)),
                ('image_sale', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]
