# Generated by Django 2.2b1 on 2019-03-03 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190303_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sampleemp',
            name='VOLUME',
        ),
        migrations.AddField(
            model_name='sampleemp',
            name='DIAMETER',
            field=models.FloatField(max_length=30, null=True),
        ),
    ]