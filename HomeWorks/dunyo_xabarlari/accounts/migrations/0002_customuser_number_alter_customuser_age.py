# Generated by Django 4.2.7 on 2023-11-24 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="number",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="age",
            field=models.PositiveIntegerField(null=True),
        ),
    ]