# Generated by Django 4.2.5 on 2023-09-20 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='floors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='occupants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupant_name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('C1', 'C1'), ('C2', 'C2')], max_length=50, null=True)),
                ('floor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='electricity.floors')),
                ('occupant_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='electricity.occupants')),
            ],
        ),
        migrations.CreateModel(
            name='electricities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('dpdc1', models.CharField(blank=True, max_length=200, null=True)),
                ('dpdc2', models.CharField(blank=True, max_length=200, null=True)),
                ('dpdc3', models.CharField(blank=True, max_length=200, null=True)),
                ('generator1', models.CharField(blank=True, max_length=200, null=True)),
                ('generator2', models.CharField(blank=True, max_length=200, null=True)),
                ('generator3', models.CharField(blank=True, max_length=200, null=True)),
                ('occupant_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='electricity.occupants')),
            ],
        ),
    ]
