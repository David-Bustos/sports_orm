from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Count

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	# SPORTS ORM I
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
	# SPORTS ORM II
		"afc_teams": Team.objects.filter(league__name="Atlantic Football Conference"),
		"boston_hawks_players": Player.objects.filter(curr_team__team_name="Hawks", curr_team__location="Boston"),
		"iwbc_players": Player.objects.filter(curr_team__league__name="International Womens' Basketball Conference"),
		"wcs_diaz_players": Player.objects.filter(curr_team__league__name="World Conference of Soccer", last_name="Diaz"),
		"soccer_players": Player.objects.filter(curr_team__league__sport="Soccer"),
		"sophia_teams": Team.objects.filter(curr_players__first_name="Sophia"),
		"sophia_leagues": League.objects.filter(teams__curr_players__first_name="Sophia"),
		"flores_players": Player.objects.filter(last_name="Flores").exclude(curr_team__team_name="Hawks", curr_team__location="Los Angeles"),
		"samuel_all_teams": Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Gonzales"),
		"st_all_players": Player.objects.filter(all_teams__team_name="Stampeders", all_teams__location="Manitoba"),
		"wv_old_players": Player.objects.filter(all_teams__team_name="Vikings", all_teams__location="Washington").exclude(curr_team__team_name="Vikings", curr_team__location="Washington"),
		"jacob_old_teams": Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Scott").exclude(curr_players__first_name="Jacob", curr_players__last_name="Scott"),
		"all_lucas_afc": Player.objects.filter(all_teams__league__name="Atlantic Football Conference",first_name="Lucas"), #Es posible agrupar?
		"gt_12p_teams": Team.objects.annotate(n_players= Count("all_players")).filter(n_players__gt=12),
		"all_players_nteams": Player.objects.annotate(n_teams= Count("all_teams")).order_by("-n_teams")
		}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")