# Generated by Django 2.2.7 on 2019-11-26 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20191126_1922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='squirrel',
            old_name='other_acivities',
            new_name='other_activities',
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='x',
            field=models.CharField(blank=True, max_length=21),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='y',
            field=models.CharField(blank=True, max_length=21),
        ),
    ]
