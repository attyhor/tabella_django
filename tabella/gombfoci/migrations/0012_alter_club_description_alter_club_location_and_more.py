# Generated by Django 4.2.5 on 2023-09-25 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gombfoci', '0011_alter_club_description_alter_club_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='club',
            name='location',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='team',
            name='club_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club_name', to='gombfoci.club'),
        ),
        migrations.AlterField(
            model_name='team',
            name='league_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='league_name_id', to='gombfoci.league'),
        ),
    ]