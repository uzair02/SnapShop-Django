# Generated by Django 4.1.1 on 2024-04-16 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pro_scrape", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scrapeddata",
            name="price",
            field=models.CharField(max_length=20),
        ),
    ]
