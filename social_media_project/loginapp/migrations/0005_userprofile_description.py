# Generated by Django 3.0.7 on 2021-02-11 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0004_userprofile_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.CharField(blank=True, max_length=264),
        ),
    ]
