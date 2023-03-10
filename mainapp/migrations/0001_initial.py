# Generated by Django 4.0.4 on 2022-06-02 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.CharField(default='', max_length=100)),
                ('bus', models.CharField(default='', max_length=100)),
                ('departure_time', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BookTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=200)),
                ('sur_name', models.CharField(default='', max_length=200)),
                ('phone_num', models.IntegerField(default=0)),
                ('email_address', models.EmailField(default='', max_length=254)),
                ('home_address', models.CharField(default='', max_length=200)),
                ('next_kin_name', models.CharField(default='', max_length=200)),
                ('next_kin_phone_num', models.IntegerField(default=0)),
                ('next_kin_home_address', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(default='', max_length=100)),
                ('bus_num', models.IntegerField(default=0, max_length=100)),
                ('from_d', models.CharField(default='', max_length=100)),
                ('to_d', models.CharField(default='', max_length=100)),
                ('departure_time', models.TimeField()),
                ('arrival_time', models.TimeField()),
                ('distance', models.FloatField(default=0.0, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(default='', max_length=100)),
                ('bus', models.CharField(choices=[('bus1', 'bus1'), ('bus2', 'bus2'), ('bus3', 'bus3')], default='bus1', max_length=100)),
                ('distance', models.FloatField(default=0.0, max_length=20)),
                ('fare', models.FloatField(default=0.0, max_length=100)),
            ],
        ),
    ]
