# Generated by Django 3.0.3 on 2020-03-11 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0002_auto_20200310_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_note',
            name='zoom',
            field=models.IntegerField(default=7),
            preserve_default=False,
        ),
    ]
