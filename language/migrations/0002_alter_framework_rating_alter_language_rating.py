# Generated by Django 4.1.2 on 2022-10-25 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='framework',
            name='rating',
            field=models.CharField(choices=[('1', '1 etoile'), ('2', '2 etoiles'), ('3', '3 etoiles'), ('4', '4 etoiles'), ('4', '5 etoiles')], default='draft', max_length=1),
        ),
        migrations.AlterField(
            model_name='language',
            name='rating',
            field=models.CharField(choices=[('1', '1 etoile'), ('2', '2 etoiles'), ('3', '3 etoiles'), ('4', '4 etoiles'), ('4', '5 etoiles')], max_length=1),
        ),
    ]
