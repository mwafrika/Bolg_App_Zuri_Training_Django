# Generated by Django 3.2 on 2021-04-22 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
