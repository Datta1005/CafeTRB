# Generated by Django 4.1.4 on 2023-01-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Burger', '0002_delete_burgerinfomodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='VegInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Burger', models.CharField(max_length=35)),
                ('prize', models.IntegerField()),
            ],
        ),
    ]
