# Generated by Django 3.1.7 on 2021-02-24 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promise_keeper', '0005_auto_20210224_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='ruling',
            field=models.ManyToManyField(blank=True, to='promise_keeper.State'),
        ),
    ]