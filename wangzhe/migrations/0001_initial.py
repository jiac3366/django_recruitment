# Generated by Django 3.0.3 on 2021-03-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('hp_max', models.FloatField(blank=True, null=True)),
                ('hp_growth', models.FloatField(blank=True, null=True)),
                ('hp_start', models.FloatField(blank=True, null=True)),
                ('mp_max', models.FloatField(blank=True, null=True)),
                ('mp_growth', models.FloatField(blank=True, null=True)),
                ('mp_start', models.FloatField(blank=True, null=True)),
                ('attack_max', models.FloatField(blank=True, null=True)),
                ('attack_growth', models.FloatField(blank=True, null=True)),
                ('attack_start', models.FloatField(blank=True, null=True)),
                ('defense_max', models.FloatField(blank=True, null=True)),
                ('defense_growth', models.FloatField(blank=True, null=True)),
                ('defense_start', models.FloatField(blank=True, null=True)),
                ('hp_5s_max', models.FloatField(blank=True, null=True)),
                ('hp_5s_growth', models.FloatField(blank=True, null=True)),
                ('hp_5s_start', models.FloatField(blank=True, null=True)),
                ('mp_5s_max', models.FloatField(blank=True, null=True)),
                ('mp_5s_growth', models.FloatField(blank=True, null=True)),
                ('mp_5s_start', models.FloatField(blank=True, null=True)),
                ('attack_speed_max', models.FloatField(blank=True, null=True)),
                ('attack_range', models.CharField(blank=True, max_length=255, null=True)),
                ('role_main', models.CharField(blank=True, max_length=255, null=True)),
                ('role_assist', models.CharField(blank=True, max_length=255, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'heros',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HerosPlay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_name', models.CharField(blank=True, max_length=255, null=True)),
                ('game_id', models.IntegerField(blank=True, null=True)),
                ('player_name', models.CharField(blank=True, max_length=255, null=True)),
                ('kda_k', models.IntegerField(blank=True, null=True)),
                ('kda_d', models.IntegerField(blank=True, null=True)),
                ('kda_a', models.IntegerField(blank=True, null=True)),
                ('money', models.IntegerField(blank=True, null=True)),
                ('damage_input', models.IntegerField(blank=True, null=True)),
                ('damage_output', models.IntegerField(blank=True, null=True)),
                ('win', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('modified_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'heros_play',
                'managed': False,
            },
        ),
    ]