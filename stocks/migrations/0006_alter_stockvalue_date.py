# Generated by Django 4.1.1 on 2022-09-22 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0005_alter_stockvalue_value_adjclose_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockvalue',
            name='date',
            field=models.DateField(),
        ),
    ]
