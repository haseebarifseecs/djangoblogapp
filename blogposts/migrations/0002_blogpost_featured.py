# Generated by Django 2.1.1 on 2019-07-08 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
