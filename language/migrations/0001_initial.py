# Generated by Django 4.1.2 on 2022-10-25 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('release_date', models.DateField()),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('HN', 'Haut niveau'), ('LA', 'Assembleur'), ('LMe', 'Machine'), ('LMl', 'Materiel')], max_length=5)),
                ('poo', models.BooleanField(default=False)),
                ('rating', models.CharField(choices=[('1', 'Une etoile'), ('2', 'Deux etoiles'), ('3', '3 etoiles'), ('4', '4 etoiles'), ('4', '5 etoiles')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('release_date', models.DateField()),
                ('description', models.TextField()),
                ('rating', models.CharField(choices=[('1', 'Une etoile'), ('2', 'Deux etoiles'), ('3', '3 etoiles'), ('4', '4 etoiles'), ('4', '5 etoiles')], default='draft', max_length=1)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='language.language')),
            ],
        ),
    ]