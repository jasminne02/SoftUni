class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    def __str__(self):
        return f"Player: {self.__name}\nSprint: {self.__sprint}\nDribble: {self.__dribble}\n" \
               f"Passing: {self.__passing}\nShooting: {self.__shooting} "

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 0:
            self.__name = value
