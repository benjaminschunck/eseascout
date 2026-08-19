import requests


def get_upcoming_matches(championship_id, api_key):
    response = requests.get(
        f"https://open.faceit.com/data/v4/championships/{championship_id}/matches",
        params={"type": "upcoming", "limit": 100},
        headers={"Authorization": f"Bearer {api_key}"}
    )
    matches = response.json()["items"]

    return matches

def get_team_stats(team_id, api_key):
    """
    Fetch a team's CS2 stats from FACEIT — win rates, matches played,
    broken down per map (in the response's "segments" field).

    Returns the raw JSON response, unprocessed.
    """
    # TODO: GET https://open.faceit.com/data/v4/teams/{team_id}/stats/cs2
    pass