def get_next_match(matches, team_id):
    """
    Given the full unfiltered list of matches (from get_upcoming_matches),
    find the single soonest match involving team_id.

    Returns a dict like:
        {"opponent_id": ..., "opponent_name": ..., "scheduled_at": ...}
    or None if there are no upcoming matches for this team.
    """
    team_matches = []
    for match in matches:
        factions = match.get("teams", {})
        faction1 = factions.get("faction1", {})
        faction2 = factions.get("faction2", {})

        if faction1.get("faction_id") == team_id:
            opponent = faction2
        elif faction2.get("faction_id") == team_id:
            opponent = faction1
        else:
            continue

        team_matches.append({
            "opponent_id": opponent.get("faction_id"),
            "opponent_name": opponent.get("name", "Unknown opponent"),
            "scheduled_at": match.get("scheduled_at", 0),
        })

    return min(team_matches, key=lambda match: match["scheduled_at"]) if team_matches else None


def get_map_win_rates(stats_response):
    """Return map names and win rates, sorted from highest to lowest."""
    return [(name, win_rate) for name, win_rate, _ in get_map_stats(stats_response)]


def get_map_stats(stats_response):
    """Return map names, win rates, and match counts sorted by win rate."""
    map_stats = []
    for segment in stats_response.get("segments", []):
        name = segment.get("label") or segment.get("name") or segment.get("segment")
        stats = segment.get("stats", {})
        win_rate = next(
            (value for key, value in stats.items() if key.lower() in {"win rate %", "win rate", "winrate"}),
            None,
        )

        wins = next((value for key, value in stats.items() if key.lower() in {"wins", "win"}), None)
        matches = next((value for key, value in stats.items() if key.lower() in {"matches", "matches played"}), None)
        if win_rate is None:
            if wins is not None and matches:
                win_rate = float(wins) / float(matches) * 100

        if name and win_rate is not None:
            match_count = int(float(matches)) if matches is not None else None
            map_stats.append((name.removeprefix("de_"), float(str(win_rate).rstrip("%")), match_count))

    return sorted(map_stats, key=lambda item: item[1], reverse=True)