# Generated by Django 3.1.2 on 2021-03-06 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_auto_20210306_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='aliment',
            name='average',
            field=models.IntegerField(default=0, null=True),
        ),
    ]