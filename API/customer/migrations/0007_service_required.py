# Generated by Django 2.1.5 on 2019-03-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20190311_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='required',
            field=models.IntegerField(default=0),
        ),
    ]
