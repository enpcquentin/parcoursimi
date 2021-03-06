# Generated by Django 2.0.5 on 2018-05-24 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('option', models.CharField(choices=[('O1', '3A Ecole'), ('O2', '3A M2 imbriques stage M2 et PFE'), ('O3', '3A M2 imbriques 3 cours supplementaires'), ('O4', '3A M2 imbriques 2 cours 1 projet')], max_length=2)),
                ('department', models.CharField(max_length=100)),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcours.Master')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcours.Master'),
        ),
    ]
