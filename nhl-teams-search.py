from sportsreference.nhl.teams import Teams

print("Team  |    Wins   |    Losses   |   Points")
for team in Teams():
    print(team.name, team.wins, team.losses, team.points)