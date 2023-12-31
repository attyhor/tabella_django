# Generated by Django 4.2.5 on 2023-09-24 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gombfoci', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_score', models.IntegerField()),
                ('guest_score', models.IntegerField()),
                ('result', models.CharField(max_length=1)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_match', to=settings.AUTH_USER_MODEL)),
                ('guest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guest_team_name', to='gombfoci.team')),
                ('home_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team_name', to='gombfoci.team')),
            ],
        ),
    ]
