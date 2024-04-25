# Generated by Django 3.2.6 on 2024-04-02 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('cookie', models.CharField(max_length=255)),
                ('facebook_id', models.CharField(max_length=255)),
                ('user_agent', models.CharField(max_length=255)),
                ('avatar', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fanpage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('fanpage_id', models.CharField(max_length=255)),
                ('fanpage_id_delegate', models.CharField(max_length=255)),
                ('avatar', models.CharField(max_length=255)),
                ('facebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.facebook')),
            ],
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('platform', models.CharField(max_length=255, null=True)),
                ('published_at', models.DateTimeField(null=True)),
                ('channel_id', models.CharField(max_length=255, null=True)),
                ('fanpage_id', models.CharField(max_length=255, null=True)),
                ('view_count', models.IntegerField(null=True)),
                ('subscribe_count', models.IntegerField(null=True)),
                ('thumbnail', models.CharField(max_length=255, null=True)),
                ('banner', models.CharField(max_length=255, null=True)),
                ('playlist_id', models.CharField(max_length=255, null=True)),
                ('checkins', models.IntegerField(null=True)),
                ('likes', models.IntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
