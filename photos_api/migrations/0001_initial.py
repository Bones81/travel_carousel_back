# Generated by Django 4.2 on 2023-04-04 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=32)),
                ('country', models.CharField(max_length=32)),
                ('comments', models.CharField(max_length=500)),
                ('image_file', models.ImageField(upload_to='photos/%Y/%m/%d')),
            ],
        ),
    ]