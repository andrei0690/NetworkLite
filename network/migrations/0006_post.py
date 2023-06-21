# Generated by Django 4.2.1 on 2023-06-09 15:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('network', '0005_alter_profile_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='profile_images')),
                ('date_posted', models.DateTimeField(default=datetime.datetime.now)),
                ('nr_of_likes', models.IntegerField()),
                ('nr_of_comments', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]