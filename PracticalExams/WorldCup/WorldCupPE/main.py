from domain.FotballTeam import FotballTeam
from infrastucture.WorldCup import cup

cup= cup()

cup.add_team(FotballTeam(8, "E"))
cup.add_team(FotballTeam(11, "H"))
cup.add_team(FotballTeam(17, "C"))
cup.add_team(FotballTeam(13, "F"))
cup.add_team(FotballTeam(15, "H"))

for i in cup.get_all():
    print(i)

print(self.add_by_index(2, FotballTeam(8, "A")))

print(self.number_of_scored_goals_is_minumum(11))
