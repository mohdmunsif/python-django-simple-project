# Generated by Django 2.2.3 on 2019-08-07 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entries',
            name='age_lower',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entries',
            name='age_upper',
            field=models.CharField(default=18, max_length=300),
            preserve_default=False,
        ),
    ]
