# Generated by Django 5.1 on 2024-09-09 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_remove_news_news_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='news/'),
        ),
    ]
