# Generated by Django 3.1.7 on 2021-02-25 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promise_keeper', '0010_auto_20210225_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='logo',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='politician',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
