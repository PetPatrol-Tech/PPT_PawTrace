# Generated by Django 4.1 on 2024-07-09 11:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Resident",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20)),
                ("phoneNumber", models.CharField(max_length=11)),
                ("date", models.DateField()),
                ("numOfPets", models.IntegerField(max_length=1)),
                ("state", models.IntegerField(max_length=1)),
            ],
        ),
    ]
