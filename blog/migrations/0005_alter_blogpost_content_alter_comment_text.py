# Generated by Django 5.0 on 2023-12-12 19:33

import markdownx.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
