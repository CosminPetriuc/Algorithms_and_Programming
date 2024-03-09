class My_Point():
    def __init__(self, x, y, color):
        self.__x = x
        self.__y = y
        self.__color = color

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def getcolor(self):
        return self.__color

    def setx(self, x):
        self.__x = x

    def sety(self, y):
        self.__y = y

    def setcolor(self, color):
        self.__color = color

    def __str__(self):
        return "Point (" + str(self.__x) + ", " + str(self.__y) + ") of color " + str(self.__color)

    def __repr__(self):
        return repr(self.__str__())

My_Point.color_list = ['red', 'green', 'blue', 'yellow', 'magenta']