# Generated by Django 5.0 on 2023-12-10 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_remove_education_current_experience_current'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
