"""
This module contains functions to make football tallys
"""

HEADER = "Team                           | MP |  W |  D |  L |  P"
STARTING = {
    "wins": 0,
    "draws": 0,
    "losses": 0,
    "played": 0,
    "points": 0
}

def tally(rows: list[str]) -> list[str]:
    """
    Given the information, will return tally

    rows: list[str] - rows with information
    return: list[str] - tally
    """

    # Empty dictionary to save results
    info = {}
    """
    Format:
    "name": {
        "wins": int
        "draws": int
        "losses": int,
        "played": int,
        "points": int
    }
    """

    # Process
    for match in rows:
        
        # Separate
        team1, team2, result = match.split(";")
        print(f"Splitted: Team 1: {team1}, Team 2: {team2}, Result: {result}")
        
        # Check if team already exists
        if team1 not in list(info.keys()):
            info[team1] = dict(STARTING)
        if team2 not in list(info.keys()):
            info[team2] = dict(STARTING)

        # Teams should exist, add info

        # Check if draw
        if result == "draw":
            # Team 1
            info[team1]["played"] += 1
            info[team1]["draws"] += 1
            info[team1]["points"] += 1
            # Team 2
            info[team2]["played"] += 1
            info[team2]["draws"] += 1
            info[team2]["points"] += 1
            continue

        # Someone won, determine it
        if result == "win":
            winning_team = team1
            losing_team = team2
        else:
            winning_team = team2
            losing_team = team1

        # Compute match
        # Winning team
        info[winning_team]["played"] += 1
        info[winning_team]["wins"] += 1
        info[winning_team]["points"] += 3
        # Losing team
        info[losing_team]["played"] += 1
        info[losing_team]["losses"] += 1
        info[losing_team]["points"] += 0

    # Proccessed info
    print("----------INFO----------")
    print(info)

    # Make info into array
    table = []
    for team in list(info.items()):
        print(team)
        t = {
            "name": team[0]
        }
        t.update(team[1])
        table.append(t)

    # Order info
    print(table)
    table.sort(key=lambda x: (-x["points"], x["name"]))
    print(table)

    # Now create tally:
    tlly = [HEADER]
    for team in table:
        tlly += [f"""{team["name"]}{"".join([ " " for i in range(31 - len(team["name"])) ])}|  {team["played"]} |  {team["wins"]} |  {team["draws"]} |  {team["losses"]} |{"".join([ " " for i in range(3 - len(str(team["points"]))) ])}{team["points"]}"""]

    print("----------TALLY----------")
    print("\n".join(tlly))
    return tlly

tally([
            "Allegoric Alaskans;Blithering Badgers;win",
            "Blithering Badgers;Courageous Californians;win",
            "Courageous Californians;Allegoric Alaskans;loss",
        ])

"""
"Team                           | MP |  W |  D |  L |  P",
"Allegoric Alaskans             |  2 |  2 |  0 |  0 |  6",
"Blithering Badgers             |  2 |  1 |  0 |  1 |  3",
"Courageous Californians        |  2 |  0 |  0 |  2 |  0",
"""