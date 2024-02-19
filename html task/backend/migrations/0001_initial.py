# Generated by Django 4.2.9 on 2024-02-05 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('rate', 'rate'), ('free', 'free')], max_length=10)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('options', models.JSONField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('nq', models.PositiveIntegerField()),
                ('qs', models.JSONField()),
            ],
        ),
    ]
