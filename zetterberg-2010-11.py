from sportsreference.nhl.roster import Player

zetterberg = Player('zettehe01')
zetterberg('2010-11')
print("Name  |  Goals  |  Assists  | Points|   Games played")
print(zetterberg.name, zetterberg.goals, zetterberg.assists, zetterberg.points, zetterberg.games_played)