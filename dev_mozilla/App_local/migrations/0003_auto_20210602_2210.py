# Generated by Django 3.1.6 on 2021-06-02 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_local', '0002_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images'),
        ),
    ]
