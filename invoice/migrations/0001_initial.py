# Generated by Django 5.0.4 on 2024-04-06 12:25

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("name", models.CharField(max_length=100, verbose_name="名前")),
                (
                    "unit_price",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="単価",
                    ),
                ),
                (
                    "order",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="並び順",
                    ),
                ),
            ],
            options={
                "verbose_name": "メニュー",
                "verbose_name_plural": "メニュー",
            },
        ),
        migrations.CreateModel(
            name="Invoice",
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
                (
                    "customer",
                    models.CharField(max_length=100, verbose_name="テーブルNoを入力してください"),
                ),
                ("sub_total", models.IntegerField(verbose_name="小計")),
                ("tax", models.IntegerField(verbose_name="消費税")),
                ("total_amount", models.IntegerField(verbose_name="合計金額")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="登録日"),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="作成者",
                    ),
                ),
            ],
            options={
                "verbose_name": "注文",
                "verbose_name_plural": "注文",
            },
        ),
        migrations.CreateModel(
            name="InvoiceDetail",
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
                (
                    "unit_price",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="単価",
                    ),
                ),
                (
                    "quantity",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="数量",
                    ),
                ),
                ("amount", models.IntegerField(verbose_name="金額")),
                (
                    "invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="invoice.invoice",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="invoice.item",
                        verbose_name="商品",
                    ),
                ),
            ],
        ),
    ]
