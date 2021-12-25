# Generated by Django 3.2.10 on 2021-12-21 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20211221_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='elevation',
            field=models.CharField(max_length=50, verbose_name='海拔'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='lattitude',
            field=models.CharField(max_length=50, verbose_name='纬度'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='longitude',
            field=models.CharField(max_length=50, verbose_name='经度'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='sample_count',
            field=models.CharField(max_length=50, verbose_name='样本数量'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='sample_total_weight',
            field=models.CharField(max_length=50, verbose_name='样本重量'),
        ),
    ]
