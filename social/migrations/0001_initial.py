# Generated by Django 5.0.2 on 2024-02-18 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredictionPauvrete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.FloatField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
