import unittest
from Domain.My_Vector import MyVector
from Repo.VectorRepo import VectorRepository

import numpy as np
from numpy.testing import assert_array_equal

class TestVectorRepository(unittest.TestCase):
    def setUp(self):
        # Initialize a VectorRepository for testing
        self.vector_repo = VectorRepository()

        # Add some sample vectors for testing
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [4, 5, 6])
        self.vector3 = MyVector(3, 'b', 3, [7, 8, 9])

        self.vector_repo.addVector(self.vector1)
        self.vector_repo.addVector(self.vector2)
        self.vector_repo.addVector(self.vector3)

    def test_getAllVectors(self):
        vectors = self.vector_repo.getAllVectors()
        self.assertEqual(len(vectors), 3)

    def test_addVector(self):
        new_vector = MyVector(4, 'y', 1, [10, 11, 12])
        self.vector_repo.addVector(new_vector)
        vectors = self.vector_repo.getAllVectors()
        self.assertEqual(len(vectors), 4)

    def test_returnVectorAtIndex(self):
        returned_vector = self.vector_repo.returnVectorAtIndex(1)
        self.assertEqual(returned_vector, self.vector2)

    def test_updateVectorAtIndex(self):
        self.vector_repo.updateVectorAtindex(0, 5, 'm', 2, [13, 14, 15])
        updated_vector = self.vector_repo.returnVectorAtIndex(0)
        self.assertEqual(updated_vector.get_name_id(), 5)
        self.assertEqual(updated_vector.get_color(), 'm')
        self.assertEqual(updated_vector.get_type(), 2)
        assert_array_equal(updated_vector.get_value(), np.array([13, 14, 15]))

    def test_updateVectorByName_id(self):
        self.vector_repo.updateVectorByName_id(2, 'b', 3, [16, 17, 18])
        updated_vector = self.vector_repo.returnVectorAtIndex(1)
        self.assertEqual(updated_vector.get_color(), 'b')
        self.assertEqual(updated_vector.get_type(), 3)
        assert_array_equal(updated_vector.get_value(), np.array([16, 17, 18]))

    def test_deleteVectorByIndex(self):
        self.vector_repo.deleteVectorByIndex(1)
        vectors = self.vector_repo.getAllVectors()
        self.assertEqual(len(vectors), 2)

    def test_deleteVectorByName_id(self):
        self.vector_repo.deleteVectorByName_id(2)
        vectors = self.vector_repo.getAllVectors()
        self.assertEqual(len(vectors), 2)

    def test_getSumOfVectorsWithAGivenColor(self):
        sum_result = self.vector_repo.getSumOfVectorsWithAGivenColor('g')
        self.assertEqual(sum_result, self.vector2.sum_of_elements())

    def test_deleteAllVectorsFromRepository(self):
        self.vector_repo.deleteAllVectorsFromRepository()
        vectors = self.vector_repo.getAllVectors()
        self.assertEqual(len(vectors), 0)

    def test_updateColorByVectorName_id(self):
        self.vector_repo.updateColorByVectorName_id(1, 'y')
        updated_vector = self.vector_repo.returnVectorAtIndex(0)
        self.assertEqual(updated_vector.get_color(), 'y')


