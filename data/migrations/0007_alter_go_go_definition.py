# Generated by Django 3.2.10 on 2021-12-22 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20211222_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='go',
            name='go_definition',
            field=models.CharField(max_length=1250, verbose_name='GO描述'),
        ),
    ]
