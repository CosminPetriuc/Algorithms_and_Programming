from domain.FotballTeam import FotballTeam
from infrastucture.WorldCup import WorldCup

WorldCup= WorldCup()

WorldCup.add_team(FotballTeam(8, "E"))
WorldCup.add_team(FotballTeam(11, "H"))
WorldCup.add_team(FotballTeam(17, "C"))
WorldCup.add_team(FotballTeam(13, "F"))
WorldCup.add_team(FotballTeam(15, "H"))

for i in WorldCup.get_all():
    print(i)

print(self.add_by_index(2, FotballTeam(8, "A")))

print(self.number_of_scored_goals_is_minumum(11))
