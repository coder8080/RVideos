# Generated by Django 3.1.5 on 2021-02-09 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201128_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='image',
            field=models.ImageField(null=True, upload_to='channel_images/', verbose_name='Картинка канала'),
        ),
    ]
