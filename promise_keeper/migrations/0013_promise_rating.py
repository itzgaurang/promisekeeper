# Generated by Django 3.1.7 on 2021-03-02 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promise_keeper', '0012_auto_20210228_0556'),
    ]

    operations = [
        migrations.AddField(
            model_name='promise',
            name='rating',
            field=models.CharField(default='', max_length=15),
        ),
    ]
