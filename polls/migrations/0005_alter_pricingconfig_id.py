# Generated by Django 3.2.12 on 2022-11-07 14:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_pricingconfig_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricingconfig',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]