from it1.Domain import My_Point
import math
import matplotlib.pyplot as plt

class MyReposetory():
    def __init__(self):
        self.__list_of_points =[]
    def __str__(self):
        return str(self.__list_of_points)

    # add a point to the list of points
    def add(self, x, y, color):
        self.__list_of_points.append(My_Point(x, y, color))

    # get the list of points
    def get_all_points(self):
        return self.__list_of_points

    # get points by their index in the list
    def get_points_index(self, index):
        return self.__list_of_points[index]

    # get the points with a specific color
    def get_points_given_color(self, color):
        return [point for point in self.__list_of_points if point.getcolor() == color]

    # get the points inside a square defined by its corners and length
    def get_points_inside_a_square(self, x_corner, y_corner, length):
        points_inside_square = MyReposetory()
        for p in self.__list_of_points:
            if (x_corner <= p.getx() <= x_corner + length and
                y_corner - length <= p.gety() <= y_corner):
                points_inside_square.add(p.getx(), p.gety(), p.getcolor())
        return points_inside_square

    # get the points inside a circle defined by its center and radius
    def delete_points_inside_a_given_circle(self, x_center, y_center, radius):
        for point in self.__list_of_points:
            if (point.getx() - x_center)**2 + (point.gety() - y_center)**2 <= radius**2:
                # the formula for the radius of a circle
                self.__list_of_points.remove(point)

    # get the minimum distance between two points
    def get_minimum_distance_between_points(self, point1, point2):
        distance = math.sqrt(
            (point1.getx() - point2.getx()) ** 2 + (point1.gety() - point2.gety()) ** 2
        ) # the formula for the distance between two points
        return distance

    # get the points inside a rectangle defined by its corners, length and width
    def get_points_inside_a_given_rectangle(self, x_corner, y_corner, length, width):
        points_inside_rectangle = MyReposetory()
        for p in self.__list_of_points:
            if (x_corner <= p.getx() <= x_corner + length and
                y_corner - width <= p.gety() <= y_corner):
                # Check if the point is inside the specified rectangle
                points_inside_rectangle.add(p.getx(), p.gety(), p.getcolor())
                # Add the point to the new repository
        return points_inside_rectangle

    # update the color of a point chosen by its coordinates
    def update_a_point_color_given_its_coordinates(self, x, y, color):
        for point in self.__list_of_points:
            if point.getx() == x and point.gety() == y:
                point.setcolor(color)

    # update a point chosen by its index in the list
    def update_a_point_by_index(self, index, x, y, color):
        self.__list_of_points[index].setx(x)
        self.__list_of_points[index].sety(y)
        self.__list_of_points[index].setcolor(color)

    # delete a point chosen by index in the list
    def delete_a_point_by_index(self, index):
        self.__list_of_points.pop(index)

    # delete all points inside a square defined by its corners and length
    def delete_points_inside_a_given_square(self, x_corner, y_corner, length):
        for point in self.__list_of_points:
            if (x_corner <= point.getx() <= x_corner + length and
                y_corner - length <= point.gety() <= y_corner):
                self.__list_of_points.remove(point)

    # plot the points from the list
    def plot_points(self):
        x = []
        y = []
        color = []
        for i in range(0,len(self.__list_of_points)):
            x.append(self.__list_of_points[i].getx())
            y.append(self.__list_of_points[i].gety())
            color.append(self.__list_of_points[i].getcolor())
        plt.scatter(x, y, c = color)
        plt.show()