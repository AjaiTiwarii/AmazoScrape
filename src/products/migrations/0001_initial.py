# Generated by Django 5.0.6 on 2024-06-22 09:55

import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(db_index=True, max_length=120, unique=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=220, null=True)),
                ('current_price', models.FloatField(blank=True, default=0.0, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('active', models.BooleanField(default=True, help_text='Scrape daily?')),
            ],
        ),
        migrations.CreateModel(
            name='ProductScrapeEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
                ('data', models.JSONField(blank=True, null=True)),
                ('asin', models.CharField(blank=True, max_length=120, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scrape_events', to='products.product')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]