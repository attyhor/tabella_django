from typing import Any
from django.shortcuts import render, get_object_or_404
from .forms import TeamForm
from .models import Team
from django.views.generic.list import ListView

# Create your views here.

def index(request):

    form = TeamForm()
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    return render(request, 'gombfoci/index.html', context)


def new_team(request):

    form = TeamForm()
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    return render(request, 'gombfoci/new_team.html', context)


def team_list(request):
    team = get_object_or_404(Team, shortname = 'Notti')
    return render(request, 'gombfoci/team_list.html', {'team': team})


def team_list2(request):
    teams = Team.objects.all()
    return render(request, 'gombfoci/team_list2.html', {'teams': teams})



class TeamListView(ListView):
    model = Team
    paginate_by = 5
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)
    

