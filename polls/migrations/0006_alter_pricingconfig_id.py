# Generated by Django 3.2.12 on 2022-11-07 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_pricingconfig_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricingconfig',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
