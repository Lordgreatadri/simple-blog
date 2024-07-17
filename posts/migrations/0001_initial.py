# Generated by Django 5.0.7 on 2024-07-14 21:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=1000000)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2024, 7, 14, 21, 3, 0, 909410))),
            ],
        ),
    ]
