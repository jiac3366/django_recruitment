# Generated by Django 3.0.3 on 2021-01-23 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='hr_communication_ability',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='坦诚沟通综合等级'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_logic_ability',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='逻辑思维综合等级'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_potential',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='发展潜力综合等级'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_responsibility',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='责任心综合等级'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_result',
            field=models.CharField(blank=True, choices=[('建议录用', '建议录用'), ('待定', '待定'), ('放弃', '放弃')], max_length=256, verbose_name='HR终面结果'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_stability',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='稳定性综合等级'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='second_remark',
            field=models.CharField(blank=True, max_length=135, verbose_name='复试备注'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='second_result',
            field=models.CharField(blank=True, choices=[('建议录用', '建议录用'), ('待定', '待定'), ('放弃', '放弃')], max_length=256, verbose_name='复试结果'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='second_score',
            field=models.DecimalField(blank=True, decimal_places=1, help_text='1-5分，极优秀: >=4.5，优秀: 4-4.4，良好: 3.5-3.9，一般: 3-3.4，较差: <3分', max_digits=2, null=True, verbose_name='复试得分'),
        ),
    ]
