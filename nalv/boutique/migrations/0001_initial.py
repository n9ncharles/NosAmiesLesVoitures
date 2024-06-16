# Generated by Django 5.0.6 on 2024-06-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=100)),
                ('serie', models.CharField(max_length=100)),
                ('categorie', models.CharField(max_length=100)),
                ('moteur', models.CharField(max_length=100)),
                ('immatriculation', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=290)),
                ('couleur', models.CharField(max_length=100)),
                ('prix', models.IntegerField()),
                ('sulg', models.SlugField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_des_voitures')),
            ],
        ),
    ]
