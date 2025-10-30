from django.urls import path

from hut_meal_Team.views import TeamList, team_detail, team_members_render

app_name = 'hut_meal_Team'

urlpatterns = [
    path('team-list', TeamList.as_view(), name='team_list'),
    path('team-detail/<int:team_id>/<title>/', team_detail, name='team_detail'),
    path('team_members', team_members_render, name='team_members')
]