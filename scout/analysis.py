import requests

def get_next_match(matches, team_id):
    """
    Given the full unfiltered list of matches (from get_upcoming_matches),
    find the single soonest match involving team_id.

    Returns a dict like:
        {"opponent_id": ..., "opponent_name": ..., "scheduled_at": ...}
    or None if there are no upcoming matches for this team.
    """
    # TODO: filter matches down to ones involving team_id
    # TODO: from those, find the one with the smallest "scheduled_at"
    #       (look up min() with a key= argument)
    pass