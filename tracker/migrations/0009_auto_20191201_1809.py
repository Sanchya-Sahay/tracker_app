# Generated by Django 2.2.7 on 2019-12-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0008_auto_20191201_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='date',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
