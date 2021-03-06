# Generated by Django 2.2.7 on 2019-11-26 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('x', models.DecimalField(blank=True, decimal_places=21, max_digits=21)),
                ('y', models.DecimalField(blank=True, decimal_places=21, max_digits=21)),
                ('unique_squirrel_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('hectare', models.CharField(blank=True, max_length=3)),
                ('shift', models.CharField(blank=True, choices=[('am', 'am'), ('pm', 'pm')], max_length=2)),
                ('date', models.CharField(blank=True, max_length=8)),
                ('hectare_squirrel_number', models.IntegerField(blank=True)),
                ('age', models.CharField(blank=True, choices=[('adult', 'adult'), ('juvenile', 'juvenile')], max_length=10)),
                ('primary_fur_color', models.CharField(blank=True, choices=[('gray', 'gray'), ('cinnamon', 'cinnamon'), ('black', 'black')], max_length=10)),
                ('location', models.CharField(blank=True, choices=[('ground plane', 'ground plane'), ('above ground', 'above ground')], max_length=20)),
                ('specific_location', models.CharField(blank=True, max_length=255)),
                ('running', models.BooleanField()),
                ('chasing', models.BooleanField()),
                ('climbing', models.BooleanField()),
                ('eating', models.BooleanField()),
                ('foraging', models.BooleanField()),
                ('other_acivities', models.CharField(blank=True, max_length=255)),
                ('kuks', models.BooleanField()),
                ('quaas', models.BooleanField()),
                ('moans', models.BooleanField()),
                ('tail_flags', models.BooleanField()),
                ('tail_twitches', models.BooleanField()),
                ('approaches', models.BooleanField()),
                ('indifferent', models.BooleanField()),
                ('runs_from', models.BooleanField()),
            ],
        ),
    ]
