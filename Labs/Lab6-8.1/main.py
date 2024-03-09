from it1.Domain import My_Point
from it2.PointReposetory import MyReposetory
from tests.Tests import Tests
import unittest

rep = MyReposetory()
option = 1

while option != 0:

    print("1: Add a point to the repository" '\n'
          "2: Get all points" '\n'
          "3: Get a point at a given index" '\n'
          "4: Get all points of a given color" '\n'
          "5: Get all points that are inside a given square" '\n'
          "6: Delete all points that are inside a given circle" '\n'
          "7: Get the minimum distance between two points" '\n'
          "8: Get all points that are inside a given rectangle" '\n'
          "9: Update a point's color given its coordinates" '\n'
          "10: Update a point at a given index" '\n'
          "11: Delete a point by index" '\n'
          "12: Delete all points that are inside a given square" '\n'
          "13: Plot all points in a chart" '\n')
    try:
        option = int(input("Choose an option: "))
    except ValueError:
        print("Option must be an intiger")
    else:
        if option == 1:
            try:
                x = float(input("Input x coordinate of the point: "))
                y = float(input("Input y coordinate of the point: "))
            except ValueError:
                print("Coordinates must be numbers")
                continue
            try:
                c = input("Input color of the point: ")
                if ((c in My_Point.color_list) == False):
                    raise ValueError()
            except ValueError:
                print("Color must be red, green, blue, magenta or yellow")
                continue
            rep.add(x, y, c)
        if option == 2:
            print(rep.get_all_points())
        if option == 3:
            try:
                index = int(input("Input an index:"))
            except ValueError:
                print("Index must be an intiger")
                continue
            try:
                print(rep.get_points_index(index))
            except IndexError:
                print("Index out of range")
        if option == 4:
            try:
                c = input("Input a color:")
                if ((c in My_Point.color_list) == False):
                    raise ValueError()
            except ValueError:
                print("Color must be red, green, blue, magenta or yellow")
                continue
            print(rep.get_points_given_color(c))
        if option == 5:
            try:
                x = float(input("Input x coordinate of the point: "))
                y = float(input("Input y coordinate of the point: "))
                l = float(input("Input a lenght: "))
            except ValueError:
                print("Values must be numbers")
                continue
            print(rep.get_points_inside_a_square(x, y, l))
        if option == 6:
            try:
                x = float(input("Input x coordinate of the point: "))
                y = float(input("Input y coordinate of the point: "))
                r = float(input("Input a radius: "))
            except ValueError:
                print("Values must be numbers")
                continue
            rep.delete_points_inside_a_given_circle(x, y, r)
        if option == 7:
            try:
                index1 = int(input("Input the index of the first point: "))
                index2 = int(input("Input the index of the second point: "))
                point1 = rep.get_points_index(index1)
                point2 = rep.get_points_index(index2)
                min_distance = rep.get_minimum_distance_between_points(point1, point2)
                print(f"Minimum distance between selected points: {min_distance}")
            except ValueError:
                print("Index must be an integer")
            except IndexError:
                print("Index out of range")
        if option == 8:
            try:
                x = float(input("Input x coordinate of the point: "))
                y = float(input("Input y coordinate of the point: "))
                l = float(input("Input a lenght: "))
                w = float(input("Input a width: "))
            except ValueError:
                print("Values must be numbers")
                continue
            print(rep.get_points_inside_a_given_rectangle(x, y, l, w))
        if option == 9:
            try:
                x = float(input("Input x coordinate of the point: "))
                y = float(input("Input y coordinate of the point: "))
            except ValueError:
                print("Coordinates must be numbers")
                continue
            try:
                c = input("Input color of the point: ")
                if ((c in My_Point.color_list) == False):
                    raise ValueError()
            except ValueError:
                print("Color must be red, green, blue, magenta or yellow")
                continue
            rep.update_a_point_color_given_its_coordinates(x, y, c)
        if option == 10:
            try:
                index = int(input("Input an index:"))
            except ValueError:
                print("Index must be an intiger")
                continue
            try:
                x = float(input("Input x coordinate of the point: "))
                y = float(input("Input y coordinate of the point: "))

            except ValueError:
                print("Coordinates must be numbers")
                continue
            try:
                c = input("Input color of the point: ")
                if ((c in My_Point.color_list) == False):
                    raise ValueError()
            except ValueError:
                print("Color must be red, green, blue, magenta or yellow")
                continue
            rep.update_a_point_by_index(index, x, y, c)
        if option == 11:
            try:
                index = int(input("Input an index:"))
            except ValueError:
                print("Index must be an intiger")
                continue
            try:
                rep.delete_point_by_index(index)
            except IndexError:
                print("Index out of range")
        if option == 12:
            try:
                x = float(input("Input x coordinate of the point: "))
                y = float(input("Input y coordinate of the point: "))
                l = float(input("Input a lenght: "))
            except ValueError:
                print("Values must be numbers")
                continue
            rep.delete_points_inside_a_given_square(x, y, l)
        if option == 13:
            rep.plot_points()

        elif option == 99:
            tests_instance = Tests()
            tests_result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(Tests))
            print("Tests run:", tests_result.testsRun)
            print("Errors:", len(tests_result.errors))
            print("Failures:", len(tests_result.failures))
            print("Success:", tests_result.wasSuccessful())



