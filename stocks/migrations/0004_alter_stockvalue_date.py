# Generated by Django 4.1.1 on 2022-09-22 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_alter_stockvalue_date_alter_stockvalue_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockvalue',
            name='date',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
