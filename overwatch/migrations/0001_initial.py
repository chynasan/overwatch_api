# Generated by Django 5.1.1 on 2024-09-24 00:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Maps",
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
                ("Name", models.CharField(max_length=25)),
                ("Description", models.CharField(max_length=500)),
                (
                    "Mode",
                    models.CharField(
                        choices=[
                            ("clash", "Clash"),
                            ("control", "Control"),
                            ("escort", "Escort"),
                            ("flashpoint", "Flashpoint"),
                            ("hybrid", "Hybrid"),
                            ("push", "Push"),
                        ],
                        default=None,
                        max_length=32,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "Name",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("PassiveAbility", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Hero",
            fields=[
                (
                    "Name",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("Description", models.CharField(max_length=500)),
                ("Abilities", models.CharField(max_length=500)),
                ("Health", models.IntegerField()),
                ("Birthday", models.DateField()),
                (
                    "Role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="Role",
                        to="overwatch.role",
                    ),
                ),
            ],
        ),
    ]
