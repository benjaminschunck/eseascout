import requests


def get_upcoming_matches(championship_id, api_key):
    response = requests.get(
        f"https://open.faceit.com/data/v4/championships/{championship_id}/matches",
        params={"type": "upcoming", "limit": 100},
        headers={"Authorization": f"Bearer {api_key}"}
    )
    matches = response.json()["items"]

    return matches

def get_next_enemy_info(championship_id, team_id, api_key):

    #1. get the team id of next opponent

    #2. get the stats of the opponent team

    #3. return the json response

    return None