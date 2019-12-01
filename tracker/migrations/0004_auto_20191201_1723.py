# Generated by Django 2.2.7 on 2019-12-01 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20191126_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squirrel',
            name='hectare',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='hectare_squirrel_number',
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='age',
            field=models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], max_length=10),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='approaches',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='chasing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='climbing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='date',
            field=models.IntegerField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='eating',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='foraging',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='indifferent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='kuks',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='location',
            field=models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='moans',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='primary_fur_color',
            field=models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], max_length=10),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='quaas',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='running',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='runs_from',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='shift',
            field=models.CharField(blank=True, choices=[('AM', 'AM'), ('PM', 'PM')], max_length=2),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='tail_flags',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='tail_twitches',
            field=models.BooleanField(default=False),
        ),
    ]