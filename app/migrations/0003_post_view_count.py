# Generated by Django 4.2.5 on 2023-10-03 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_tag_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
