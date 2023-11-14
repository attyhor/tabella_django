# Generated by Django 4.2.5 on 2023-09-30 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gombfoci', '0012_alter_club_description_alter_club_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='league_id',
        ),
        migrations.RemoveField(
            model_name='team',
            name='league_id',
        ),
        migrations.AddField(
            model_name='match',
            name='season_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='season_name', to='gombfoci.season'),
        ),
        migrations.AddField(
            model_name='season',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='season',
            name='draw_points',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='season',
            name='end_year',
            field=models.PositiveIntegerField(default=1901),
        ),
        migrations.AddField(
            model_name='season',
            name='lost_points',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='season',
            name='start_year',
            field=models.PositiveIntegerField(default=1900),
        ),
        migrations.AddField(
            model_name='season',
            name='win_points',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='season_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='season_name_id', to='gombfoci.season'),
        ),
        migrations.AlterField(
            model_name='championship',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.DeleteModel(
            name='League',
        ),
    ]
