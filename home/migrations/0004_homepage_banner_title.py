# Generated by Django 2.2.7 on 2019-11-29 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
