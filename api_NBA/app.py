from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()

def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    return links

def get_Scoreboard():
    scoreboards = get_links()['currentScoreboard']
    data = get(BASE_URL + scoreboards).json()['games']

    for game in data:
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        period = game['period']
        print('---------------------------------')
        print(f"{home_team['triCode']} vs {away_team['triCode']}")
        print(f"{home_team['score']} - {away_team['score']}")
        print(f"{clock} - {period['current']}")

def get_stats():
    stats = get_links()['leagueTeamStatsLeaders']
    teams = get(BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']

    teams = list(filter(lambda x: x['name'] != "Team", teams))
    

    for team in teams:
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg']
        print(f"{name} - {nickname} - {ppg}")

get_stats()