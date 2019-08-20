# Generated by Django 2.2.4 on 2019-08-20 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarryOn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('attack', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('carry_on', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='carry_on', to='flights.CarryOn')),
                ('personal_item', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='personal_item', to='flights.CarryOn')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.Flight')),
                ('passenger', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='flights.Passenger')),
            ],
        ),
    ]
