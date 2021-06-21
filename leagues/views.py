from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseball_leagues": League.objects.filter(sport="Baseball"),
		"women_leagues": League.objects.filter(name__contains="women"),
		"hockey_leagues": League.objects.filter(sport__contains="hockey"),
		"no_football_leagues": League.objects.exclude(sport="Football"),
		"conference_leagues":League.objects.filter(name__contains="conference"),
		"atlantic_leagues":League.objects.filter(name__contains="atlantic"),
		"dallas_teams":Team.objects.filter(location="Dallas"),
		"raptors_teams":Team.objects.filter(team_name__contains="raptors"),
		"city_teams":Team.objects.filter(location__contains="city"),
		"t_teams":Team.objects.filter(team_name__startswith="t"),
		"order_location_teams":Team.objects.all().order_by("location"),
		"order_name_teams":Team.objects.all().order_by("-team_name"),
		"cooper_players":Player.objects.filter(last_name="Cooper"),
		"joshua_players":Player.objects.filter(first_name="Joshua"),
		"cooper_s_players":Player.objects.filter(last_name="Cooper").exclude(first_name__startswith="s"),
		"alexander_wyatt_players":Player.objects.filter(Q(first_name='Alexander') | Q(first_name='Wyatt')),
		
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")