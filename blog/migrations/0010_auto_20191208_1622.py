# Generated by Django 2.2.8 on 2019-12-08 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blogdetailpage_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogdetailpage',
            old_name='blog_image',
            new_name='banner_image',
        ),
    ]