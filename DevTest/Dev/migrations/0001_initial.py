# Generated by Django 3.1.5 on 2021-12-19 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='', max_length=50)),
                ('prenom', models.CharField(default='', max_length=50)),
                ('Date_Naissance', models.DateField(default='', null=True)),
                ('sex', models.CharField(default='', max_length=6)),
                ('groupe_Sanguin', models.CharField(default='', max_length=3)),
                ('Date_Consultation', models.DateField(default='', null=True)),
                ('Poids', models.FloatField(default='')),
                ('Tension', models.CharField(default='', max_length=20)),
                ('Taille', models.FloatField(default='')),
                ('Observation', models.CharField(default='', max_length=250)),
            ],
        ),
    ]
