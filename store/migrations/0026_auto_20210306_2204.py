# Generated by Django 3.1.2 on 2021-03-06 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_auto_20201204_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='aliment',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aliment',
            name='notation',
            field=models.IntegerField(null=True),
        ),
    ]