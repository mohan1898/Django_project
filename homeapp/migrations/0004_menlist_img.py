# Generated by Django 4.2.9 on 2024-01-30 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0003_men_menlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='menlist',
            name='img',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
    ]
