from django.views.generic.list import ListView

from django.shortcuts import render

from hut_meal_Team.models import Team


# Create your views here.


class TeamList(ListView):
    template_name = 'team-grid-wrs.html'
    paginate_by = 5
    def get_queryset(self):
        return Team.objects.get_queryset()



def team_detail(request, *args, **kwargs):
    team_id = kwargs['team_id']
    teams = Team.objects.filter(id=team_id).first()
    context = {
        'team': teams
    }
    return render(request, 'teamm-detail.html', context)

def team_members_render(request):
    team = Team.objects.all()[:4]
    context = {
        'team': team
    }
    return render(request, 'team_members_render.html', context)
