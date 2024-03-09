from unittest import TestCase
from infrastucture.WorldCup import WorldCup
from domain.FotballTeam import FotballTeam

def Test(unittest.TestCase):
    WorldCup = WorldCup()

    WorldCup.add_team(FotballTeam(8, "E"))
    WorldCup.add_team(FotballTeam(11, "H"))
    WorldCup.add_team(FotballTeam(17, "C"))
    WorldCup.add_team(FotballTeam(13, "F"))
    WorldCup.add_team(FotballTeam(15, "H"))
    assertEqual(11)


