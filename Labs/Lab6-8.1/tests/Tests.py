from it2.PointReposetory import MyReposetory
from it1.Domain import My_Point
import unittest


class Tests(unittest.TestCase):
    def test_add(self):
        my_object = MyReposetory()
        my_object.add(1, 2, 'red')

        self.assertEqual(len(my_object._MyReposetory__list_of_points), 1)
        self.assertEqual(my_object._MyReposetory__list_of_points[0].getx(), 1)
        self.assertEqual(my_object._MyReposetory__list_of_points[0].gety(), 2)
        self.assertEqual(my_object._MyReposetory__list_of_points[0].getcolor(), 'red')

    def test_get_all_points(self):
        my_object = MyReposetory()
        my_object.add(1, 2, 'red')
        my_object.add(3, 4, 'blue')
        my_object.add(5, 6, 'green')
        my_object.add(7, 8, 'red')
        my_object.add(9, 10, 'blue')
        my_object.add(11, 12, 'green')

        self.assertEqual(my_object.get_all_points(), my_object._MyReposetory__list_of_points)

    def test_get_points_index_valid_index(self):
        my_object = MyReposetory()
        my_object.add(1, 2, 'red')
        my_object.add(3, 4, 'blue')

        # Retrieve points by their index
        point1 = my_object.get_points_index(0)
        point2 = my_object.get_points_index(1)

        # Check if the retrieved points have the expected coordinates and color
        self.assertEqual(point1.getx(), 1)
        self.assertEqual(point1.gety(), 2)
        self.assertEqual(point1.getcolor(), 'red')

        self.assertEqual(point2.getx(), 3)
        self.assertEqual(point2.gety(), 4)
        self.assertEqual(point2.getcolor(), 'blue')

    def test_get_points_given_color(self):
        my_object = MyReposetory()
        my_object.add(1, 2, 'red')
        my_object.add(3, 4, 'blue')

        # Retrieve points with the color 'red'
        red_points = my_object.get_points_given_color('red')

        # Check if the list contains the expected point with the specified color
        self.assertEqual(len(red_points), 1)
        self.assertEqual(red_points[0].getx(), 1)
        self.assertEqual(red_points[0].gety(), 2)
        self.assertEqual(red_points[0].getcolor(), 'red')

    def test_get_points_inside_a_square(self):
        my_object = MyReposetory()
        my_object.add(1, 2, 'red')
        my_object.add(3, 4, 'blue')
        my_object.add(5, 6, 'green')

        # Retrieve points inside a square
        square_points = my_object.get_points_inside_a_square(1, 2, 4)

        # Check if the list contains the expected points inside the square
        self.assertEqual(len(square_points._MyReposetory__list_of_points), 1)
        self.assertEqual(square_points._MyReposetory__list_of_points[0].getx(), 1)
        self.assertEqual(square_points._MyReposetory__list_of_points[0].gety(), 2)
        self.assertEqual(square_points._MyReposetory__list_of_points[0].getcolor(), 'red')


    def test_delete_points_inside_a_given_circle(self):
        my_object = MyReposetory()
        my_object.add(1, 2, 'red')
        my_object.add(3, 4, 'blue')
        my_object.add(5, 6, 'green')

        # Delete points inside a circle
        my_object.delete_points_inside_a_given_circle(0, 0, 5)

        # Check if the list contains the expected points after deletion
        self.assertEqual(len(my_object._MyReposetory__list_of_points), 2)
        self.assertEqual(my_object._MyReposetory__list_of_points[0].getx(), 3)
        self.assertEqual(my_object._MyReposetory__list_of_points[0].gety(), 4)
        self.assertEqual(my_object._MyReposetory__list_of_points[0].getcolor(), 'blue')

    def test_get_minimum_distance_between_points(self):
        my_object = MyReposetory()
        point1 = My_Point(1, 2, 'red')
        point2 = My_Point(4, 6, 'blue')

        # Calculate minimum distance between two points
        distance = my_object.get_minimum_distance_between_points(point1, point2)

        # Check if the calculated distance is as expected
        self.assertAlmostEqual(distance, 5.0, places=2)


    def test_update_a_point_color_given_its_coordinates(self):
        my_object = MyReposetory()
        my_object.add(1, 2, 'red')

        # Update the color of a point given its coordinates
        my_object.update_a_point_color_given_its_coordinates(1, 2, 'green')

        # Check if the color of the point is updated as expected
        updated_point = my_object._MyReposetory__list_of_points[0]
        self.assertEqual(updated_point.getcolor(), 'green')

    def test_update_a_point_by_index(self):
        my_object = MyReposetory()
        my_object.add(1, 2, 'red')
        my_object.add(3, 4, 'blue')

        # Update a point by its index
        my_object.update_a_point_by_index(1, 5, 6, 'green')

        # Check if the point is updated as expected
        updated_point = my_object._MyReposetory__list_of_points[1]
        self.assertEqual(updated_point.getx(), 5)
        self.assertEqual(updated_point.gety(), 6)
        self.assertEqual(updated_point.getcolor(), 'green')

    def test_delete_a_point_by_index(self):
        my_object = MyReposetory()
        my_object.add(1, 2, 'red')
        my_object.add(3, 4, 'blue')

        # Delete a point by its index
        my_object.delete_a_point_by_index(0)

        # Check if the point is deleted as expected
        self.assertEqual(len(my_object._MyReposetory__list_of_points), 1)
        remaining_point = my_object._MyReposetory__list_of_points[0]
        self.assertEqual(remaining_point.getx(), 3)
        self.assertEqual(remaining_point.gety(), 4)
        self.assertEqual(remaining_point.getcolor(), 'blue')

    def test_delete_points_inside_a_given_square(self):
        my_object = MyReposetory()
        my_object.add(1, 2, 'red')
        my_object.add(3, 4, 'blue')
        my_object.add(5, 6, 'green')

        # Delete points inside a square
        my_object.delete_points_inside_a_given_square(0, 0, 4)

        # Check if the list contains the expected points after deletion
        self.assertEqual(len(my_object._MyReposetory__list_of_points), 3)
        self.assertEqual(my_object._MyReposetory__list_of_points[0].getx(), 1)
        self.assertEqual(my_object._MyReposetory__list_of_points[0].gety(), 2)
        self.assertEqual(my_object._MyReposetory__list_of_points[0].getcolor(), 'red')


