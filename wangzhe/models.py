# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Heros(models.Model):
    name = models.CharField(max_length=255)
    hp_max = models.FloatField(blank=True, null=True)
    hp_growth = models.FloatField(blank=True, null=True)
    hp_start = models.FloatField(blank=True, null=True)
    mp_max = models.FloatField(blank=True, null=True)
    mp_growth = models.FloatField(blank=True, null=True)
    mp_start = models.FloatField(blank=True, null=True)
    attack_max = models.FloatField(blank=True, null=True)
    attack_growth = models.FloatField(blank=True, null=True)
    attack_start = models.FloatField(blank=True, null=True)
    defense_max = models.FloatField(blank=True, null=True)
    defense_growth = models.FloatField(blank=True, null=True)
    defense_start = models.FloatField(blank=True, null=True)
    hp_5s_max = models.FloatField(blank=True, null=True)
    hp_5s_growth = models.FloatField(blank=True, null=True)
    hp_5s_start = models.FloatField(blank=True, null=True)
    mp_5s_max = models.FloatField(blank=True, null=True)
    mp_5s_growth = models.FloatField(blank=True, null=True)
    mp_5s_start = models.FloatField(blank=True, null=True)
    attack_speed_max = models.FloatField(blank=True, null=True)
    attack_range = models.CharField(max_length=255, blank=True, null=True)
    role_main = models.CharField(max_length=255, blank=True, null=True)
    role_assist = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'heros'
        # app_label = 'wangzhe'


class HerosPlay(models.Model):
    hero_name = models.CharField(max_length=255, blank=True, null=True)
    game_id = models.IntegerField(blank=True, null=True)
    player_name = models.CharField(max_length=255, blank=True, null=True)
    kda_k = models.IntegerField(blank=True, null=True)
    kda_d = models.IntegerField(blank=True, null=True)
    kda_a = models.IntegerField(blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)
    damage_input = models.IntegerField(blank=True, null=True)
    damage_output = models.IntegerField(blank=True, null=True)
    win = models.IntegerField(blank=True, null=True)
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    # creator = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'heros_play'
        unique_together = (('hero_name', 'game_id'), ('hero_name', 'game_id'),)
        # app_label = 'wangzhe'
