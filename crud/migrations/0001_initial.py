# Generated by Django 4.2.14 on 2024-09-22 10:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('author', models.CharField(max_length=30)),
                ('year_of_publish', models.SmallIntegerField()),
            ],
        ),
    ]
