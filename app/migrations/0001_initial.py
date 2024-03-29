# Generated by Django 4.2.6 on 2023-12-07 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('Country_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Capitals',
            fields=[
                ('Capital_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Country_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.country')),
            ],
        ),
    ]
