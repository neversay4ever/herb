# Generated by Django 3.2.10 on 2021-12-22 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_alter_go_go_definition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ssr',
            name='ssr_type',
            field=models.TextField(verbose_name='SSR类型'),
        ),
    ]
