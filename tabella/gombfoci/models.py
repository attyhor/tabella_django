from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=150)
    founded = models.PositiveIntegerField(default=2000)
    active = models.BooleanField(default=True)
    description = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=150, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Championship(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500, blank=True)
    start_year = models.PositiveIntegerField(default=1900)
    end_year = models.PositiveIntegerField(default=1901)
    championship_id = models.ForeignKey(Championship, on_delete=models.CASCADE, related_name='champ_name')
    win_points = models.PositiveIntegerField(default=0)
    lost_points = models.PositiveIntegerField(default=0)
    draw_points = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name

'''
class League(models.Model):
    name = models.CharField(max_length=150)
    season_id = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='season_name')

    def __str__(self):
        # return self.name
        return '%s %s'  % (self.name, self.season_id)
    
    def _get_full_name(self):
        "Returns the person's full name."
        return '%s, %s %s' % (self.name, self.season_id)
    full_name = property(_get_full_name)
'''


class Team(models.Model):
    name = models.CharField(max_length=150)
    club_id = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='club_name')
    shortname = models.CharField(max_length=6)
    # points = models.IntegerField()
    active = models.BooleanField(default=True)
    season_id = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='season_name_id', default=None)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name']),]

    def __str__(self):
        return self.name


class Match(models.Model):


    class Result(models.TextChoices):
        HOME = 'H', 'Home'
        GUEST = 'G', 'Guest'
        DRAW = 'D', 'Draw'


    home_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team_name')
    guest_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='guest_team_name')
    season_id = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='season_name', default=None)
    round_number = models.PositiveIntegerField(default=0)
    home_score = models.PositiveIntegerField(default=0)
    guest_score = models.PositiveIntegerField(default=0)
    result = models.CharField(max_length=1, choices=Result.choices, default=Result.DRAW)
    home_wo = models.BooleanField(default=False)
    guest_wo = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_match')
    home_check = models.BooleanField(default=False)
    guest_check = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)