# Generated by Django 2.2.7 on 2019-12-01 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20191201_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='date',
            field=models.IntegerField(null=True),
        ),
    ]
