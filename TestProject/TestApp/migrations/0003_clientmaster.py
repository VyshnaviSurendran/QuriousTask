# Generated by Django 4.0.6 on 2022-07-17 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0002_coordinator_inspector'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SLNo', models.IntegerField()),
                ('ClientName', models.CharField(max_length=20)),
                ('Location', models.CharField(max_length=50)),
            ],
        ),
    ]