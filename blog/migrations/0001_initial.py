# Generated by Django 4.2.7 on 2023-12-06 12:55

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("course_count", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("author", models.CharField(max_length=250)),
                ("preview", models.ImageField(upload_to="preview/")),
                ("is_free", models.BooleanField()),
                ("has_discount", models.BooleanField()),
                ("original_price", models.IntegerField(default=0)),
                ("discount_price", models.IntegerField(default=0)),
                (
                    "language",
                    models.CharField(
                        choices=[("Uz", "Uzbek"), ("Ru", "Russian"), ("En", "English")],
                        max_length=200,
                    ),
                ),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("Low", "Low"),
                            ("Middle", "Middle"),
                            ("High", "High"),
                        ],
                        max_length=200,
                    ),
                ),
                ("average_rating", models.IntegerField(default=0)),
                ("module_count", models.IntegerField(default=0)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.category"
                    ),
                ),
                (
                    "is_completed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="course_is_completed",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "is_purchased",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="course_is_purchased",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "is_saved",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="course_is_saved",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("image", models.ImageField(upload_to="news/")),
                ("description", models.TextField()),
                ("content", ckeditor.fields.RichTextField()),
                ("views", models.IntegerField(default=0)),
                ("twitter_link", models.URLField()),
                ("facebook_link", models.URLField()),
                ("telegram_link", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Module",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("lesson_count", models.IntegerField(default=0)),
                ("order", models.IntegerField(default=0)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.course"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("video_url", models.URLField()),
                ("preview", models.ImageField(upload_to="lesson_preview/")),
                ("description", ckeditor.fields.RichTextField()),
                ("order", models.IntegerField(default=0)),
                (
                    "bookmark",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookmark",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "is_watched",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "module",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.module"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rating", models.IntegerField()),
                ("content", models.TextField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.course"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
