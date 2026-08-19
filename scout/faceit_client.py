def get_upcoming_matches(championship_id, team_id, api_key):
    response = requests.get(
        f"https://open.faceit.com/data/v4/championships/{championship_id}/matches",
        params={"type": "upcoming", "limit": 100},
        headers={"Authorization": f"Bearer {api_key}"}
    )
    matches = response.json()["items"]

    return matches