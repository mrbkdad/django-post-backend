# Generated by Django 4.1.5 on 2023-01-10 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "commonmodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="common.commonmodel",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("content", models.TextField()),
            ],
            bases=("common.commonmodel",),
        ),
    ]
