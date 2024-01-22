# Generated by Django 4.2.9 on 2024-01-21 22:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('qualification', models.CharField(blank=True, max_length=500)),
                ('profile', models.TextField(max_length=1000)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trainers', to='website.category')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('course_date', models.DateField(blank=True, verbose_name=datetime.date)),
                ('duration', models.DurationField(blank=True, max_length=2)),
                ('overview', models.TextField(blank=True, max_length=1000)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='courses', to='website.category')),
                ('country', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='courses', to='website.country')),
                ('trainers', models.ManyToManyField(related_name='courses', to='website.trainer')),
            ],
            options={
                'ordering': ['-course_date'],
            },
        ),
    ]
