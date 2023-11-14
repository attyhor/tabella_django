from django.urls import path
from . import views
from .views import TeamListView

urlpatterns = [
    path('', views.index),
    path('new_team', views.new_team),
    #path('team_list', views.team_list),
    path('team_list', TeamListView.as_view(), name="team-list"),
    path('team_list2', views.team_list2, name="team-list2"),
]
