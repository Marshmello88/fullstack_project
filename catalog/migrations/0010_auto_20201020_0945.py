# Generated by Django 3.1.1 on 2020-10-20 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20201013_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='stars',
            field=models.IntegerField(),
        ),
    ]