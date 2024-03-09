from domain.FotballTeam import FotballTeam
class WorldCup:
    def __init__(self):
        self.__cup = []

    def add_team(self, team):
        self.__cup.append(team)

    def get_all(self):
        return self.__cup

    def add_by_index(self, index, team):
        if index < 0 or index > len(self.__cup):
            raise IndexError("index error")
        else:
            self.__cup.insert(index, team)



    def scored_goals(self, score):
        for score in range(0, len(self.__cup)):
            if score < 0:
                raise ValueError("Score must be grater than 0")

    def number_of_scored_goals_is_minumum(self,team, score):
        for score in range(0, len(self.__cup)):
            if score < 0:
                raise ValueError("Score must be grater than 0")
        else:
            self.__cup.insert(team, score)

