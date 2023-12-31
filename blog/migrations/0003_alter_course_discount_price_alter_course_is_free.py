# Generated by Django 4.2.7 on 2023-12-11 08:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_news_views"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="discount_price",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="course",
            name="is_free",
            field=models.BooleanField(verbose_name="self"),
        ),
    ]
