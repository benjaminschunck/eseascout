def get_upcoming_matches(championship_id, team_id, api_key):
    response = requests.get(
        f"https://open.faceit.com/data/v4/championships/{championship_id}/matches",
        params={"type": "upcoming", "limit": 100},
        headers={"Authorization": f"Bearer {api_key}"}
    )
    matches = response.json()["items"]

    upcoming_matches = []

    for match in matches:
        faction1 = match["teams"]["faction1"]
        faction2 = match["teams"]["faction2"]

        if faction1["faction_id"] == team_id:
            us, opponent = faction1, faction2
        elif faction2["faction_id"] == team_id:
            us, opponent = faction2, faction1
        else:
            continue

        timestamp = match["scheduled_at"]
        upcoming_matches.append({
            "us": us["name"],
            "opponent": opponent["name"],
            "timestamp": timestamp
        })

    return upcoming_matches