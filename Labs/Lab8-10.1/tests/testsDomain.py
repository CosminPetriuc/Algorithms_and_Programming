import numpy as np
import unittest
from Domain.My_Vector import MyVector

class TestMyVector(unittest.TestCase):
    def setUp(self):
        # Create an instance of MyVector for testing
        self.vector = MyVector(1, 'r', 1, [1, 2, 3])

    def test_add_scalar_to_vector(self):
        self.vector.add_scalar_to_vector(2)
        np.testing.assert_array_equal(self.vector.get_value(), [3, 4, 5])

    def test_add_two_vectors(self):
        other_vector = MyVector(2, 'g', 1, [2, 3, 4])
        self.vector.add_two_vectors(other_vector)
        np.testing.assert_array_equal(self.vector.get_value(), [3, 5, 7])

    def test_subtract_two_vectors(self):
        other_vector = MyVector(2, 'g', 1, [2, 3, 4])
        self.vector.subtract_two_vectors(other_vector)
        np.testing.assert_array_equal(self.vector.get_value(),[-1, -1, -1])

    def test_multiply_two_vectors(self):
        other_vector = MyVector(2, 'g', 1, [2, 3, 4])
        self.vector.multiply_two_vectors(other_vector)
        np.testing.assert_array_equal(self.vector.get_value(), [2, 6, 12])

    def test_sum_of_elements(self):
        self.assertEqual(self.vector.sum_of_elements(), 6)

    def test_product_of_elements(self):
        self.assertEqual(self.vector.product_of_elements(), 6)

    def test_average_of_elements(self):
        self.assertEqual(self.vector.average_of_elements(), 2.0)

    def test_min_of_vector(self):
        self.assertEqual(self.vector.min_of_vector(), 1)

    def test_max_of_vector(self):
        self.assertEqual(self.vector.max_of_vector(), 3)
