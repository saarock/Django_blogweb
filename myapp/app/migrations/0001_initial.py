# Generated by Django 4.1.7 on 2023-10-08 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.CharField(max_length=1000)),
                ('blogid', models.IntegerField()),
            ],
        ),
    ]
