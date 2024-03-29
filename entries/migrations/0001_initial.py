# Generated by Django 2.2.3 on 2019-08-07 00:57

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
            name='Entries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toyname', models.CharField(max_length=50)),
                ('descr', models.TextField()),
                ('url', models.CharField(max_length=300)),
                ('image_path', models.CharField(max_length=300)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entryusername', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
