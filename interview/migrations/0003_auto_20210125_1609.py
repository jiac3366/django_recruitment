# Generated by Django 3.0.3 on 2021-01-25 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0002_auto_20210123_2028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidate',
            options={'permissions': [('export', 'Can export candidate list'), ('notify', 'notify interviewer for candidate review')], 'verbose_name': '候选人', 'verbose_name_plural': '候选人'},
        ),
    ]
