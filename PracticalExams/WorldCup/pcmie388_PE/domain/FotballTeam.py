class FotballTeam:
    def __init__(self, scoredGoals, group):
        self.__scoreGoals = scoredGoals
        self.__group = group

    def get_score_goals(self):
        return self.__scoreGoals
    def get_group(self):
        return self.__group
    def set_score_goals(self, score):
        self.__scoreGoals = score
    def set_group(self, group):
        self.__group = group
    def __str__(self):
        return "Score goals: " + str(self.__scoreGoals) + " Group: " + self.__group