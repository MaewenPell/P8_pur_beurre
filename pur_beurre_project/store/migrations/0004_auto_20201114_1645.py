# Generated by Django 3.1.3 on 2020-11-14 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20201114_1607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aliment',
            old_name='sel',
            new_name='salt',
        ),
    ]
