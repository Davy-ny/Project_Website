# Generated by Django 4.2 on 2023-04-05 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=30)),
                ('handler', models.CharField(max_length=30)),
                ('number', models.IntegerField()),
                ('date', models.CharField(max_length=30)),
            ],
        ),
    ]
