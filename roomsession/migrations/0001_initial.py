# Generated by Django 4.0.5 on 2023-02-04 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomEntry',
            fields=[
                ('room_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('room_type', models.CharField(choices=[('RS', 'Restaurant')], max_length=2)),
                ('result_number', models.IntegerField()),
                ('result_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('preference_list', models.TextField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomsession.roomentry')),
            ],
        ),
    ]
