# Generated by Django 2.2.5 on 2019-11-01 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codearena', '0004_solution'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='codearena.Event'),
        ),
    ]