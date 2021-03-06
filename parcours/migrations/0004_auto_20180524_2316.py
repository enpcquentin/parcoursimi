# Generated by Django 2.0.5 on 2018-05-24 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcours', '0003_auto_20180524_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='days',
            field=models.CharField(choices=[('Mo', 'Lundi'), ('Tu', 'Mardi'), ('We', 'Mercredi'), ('Th', 'Jeudi'), ('Fr', 'Vendredi')], default=0, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courses',
            name='duration',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courses',
            name='semester',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
