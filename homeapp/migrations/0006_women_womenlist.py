# Generated by Django 4.2.9 on 2024-02-04 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0005_alter_menlist_men'),
    ]

    operations = [
        migrations.CreateModel(
            name='Women',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Womenlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=80)),
                ('price', models.IntegerField()),
                ('img', models.ImageField(null=True, upload_to='pics')),
                ('women', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeapp.women')),
            ],
        ),
    ]
