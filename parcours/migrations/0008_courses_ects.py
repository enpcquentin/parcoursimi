# Generated by Django 2.0.5 on 2018-05-25 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcours', '0007_auto_20180525_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='ects',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
