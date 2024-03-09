from Domain.My_Vector import MyVector
from Repo.VectorRepo import VectorRepository
from tests.tests import TestVectorRepository
from tests.testsDomain import TestMyVector
import unittest

class VectorUI:

    vector_repository = VectorRepository()

    vector_repository.addVector(MyVector(1, 'r', 1, [1, 2, 3]))
    vector_repository.addVector(MyVector(2, 'g', 2, [4, 5, 6]))
    vector_repository.addVector(MyVector(3, 'b', 3, [7, 8, 9]))
    vector_repository.addVector(MyVector(4, 'y', 4, [10, 11, 12]))
    vector_repository.addVector(MyVector(5, 'm', 5, [13, 14, 15]))
    vector_repository.addVector(MyVector(6, 'r', 1, [16, 17, 18]))
    vector_repository.addVector(MyVector(7, 'g', 2, [19, 20, 21]))
    vector_repository.addVector(MyVector(8, 'b', 3, [22, 23, 24]))
    vector_repository.addVector(MyVector(9, 'y', 4, [25, 26, 27]))
    vector_repository.addVector(MyVector(10, 'm', 5, [28, 29, 30]))

    def display_menu(self):
        print("\nMenu:")
        print("1. Add Vector")
        print("2. Update Vector by Index")
        print("3. Update Vector by Name/ID")
        print("4. Delete Vector by Index")
        print("5. Delete Vector by Name/ID")
        print("6. Get Sum of Vectors with a Given Color")
        print("7. Delete All Vectors from Repository")
        print("8. Update Color by Vector Name/ID")
        print("9. Get all Vectors")
        print("10. Get Vector by Index")
        print("11. Plot Vectors")
        print("0. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_vector()
            elif choice == "2":
                self.update_vector_by_index()
            elif choice == "3":
                self.update_vector_by_name_id()
            elif choice == "4":
                self.delete_vector_by_index()
            elif choice == "5":
                self.delete_vector_by_name_id()
            elif choice == "6":
                self.get_sum_of_vectors_with_color()
            elif choice == "7":
                self.delete_all_vectors()
            elif choice == "8":
                self.update_color_by_name_id()
            elif choice == "9":
                self.display_all_vectors()
            elif choice == "10":
                self.get_vector_by_index()
            elif choice == "11":
                self.plot_vectors()
            elif choice == "99":
                self.run_tests()
            elif choice == "98":
                self.Run_tests()
            elif choice == "0":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_vector(self):

        name_id = input("Enter Name/ID: ")
        color = input("Enter Color: ")
        v_type = input("Enter Type: ")

        values_input = input("Enter Values (comma-separated): ")
        values = [float(val) for val in values_input.split(',')]

        new_vector = MyVector(name_id, color, v_type, *values)
        self.vector_repository.addVector(new_vector)
        print("Vector added successfully.")

    def update_vector_by_index(self):
        # Get index and new vector details from the user and update the vector in the repository
        index = int(input("Enter the index of the vector to update: "))
        if 0 <= index < len(self.vector_repository):
            name_id = input("Enter New Name/ID: ")
            color = input("Enter New Color: ")
            v_type = input("Enter New Type: ")
            value = str(input("Enter New Value: "))

            self.vector_repository.updateVectorAtindex(index, name_id, color, v_type, value)
            print("Vector updated successfully.")
        else:
            print("Invalid index.")

    def update_vector_by_name_id(self):
        # Get name/ID and new vector details from the user and update the vector in the repository
        name_id = input("Enter Name/ID of the vector to update: ")
        self.vector_repository.updateVectorByName_id(name_id, input("Enter New Color: "),
                                                     input("Enter New Type: "),
                                                     float(input("Enter New Value: ")))
        print("Vector updated successfully.")

    def delete_vector_by_index(self):
        # Get index from the user and delete the vector from the repository
        index = int(input("Enter the index of the vector to delete: "))
        if 0 <= index < len(self.vector_repository):
            self.vector_repository.deleteVectorByIndex(index)
            print("Vector deleted successfully.")
        else:
            print("Invalid index.")

    def delete_vector_by_name_id(self):
        # Get name/ID from the user and delete the vector from the repository
        name_id = input("Enter Name/ID of the vector to delete: ")
        self.vector_repository.deleteVectorByName_id(name_id)
        print("Vector deleted successfully.")

    def get_sum_of_vectors_with_color(self):
        # Get color from the user and display the sum of vectors with that color
        color = input("Enter Color to get the sum of vectors: ")
        total_sum = self.vector_repository.getSumOfVectorsWithAGivenColor(color)
        print(f"Sum of vectors with color {color}: {total_sum}")

    def delete_all_vectors(self):
        # Delete all vectors from the repository
        self.vector_repository.deleteAllVectorsFromRepository()
        print("All vectors deleted successfully.")

    def update_color_by_name_id(self):
        # Get name/ID and new color from the user and update the color in the repository
        name_id = input("Enter Name/ID of the vector to update color: ")
        color = input("Enter New Color: ")
        self.vector_repository.updateColorByVectorName_id(name_id, color)
        print("Vector color updated successfully.")

    def display_all_vectors(self):
        all_vectors = self.vector_repository.getAllVectors()
        if all_vectors:
            print("\nAll Vectors:")
            for vector in all_vectors:
                print(vector)
        else:
            print("No vectors in the repository.")

    def get_vector_by_index(self):
        index = int(input("Enter the index of the vector to get: "))
        if 0 <= index < len(self.vector_repository):
            print(self.vector_repository.returnVectorAtIndex(index))
        else:
            print("Invalid index.")

    def plot_vectors(self):
        self.vector_repository.plotVectors()

    def run_tests(self):
        test_suite = unittest.TestLoader().loadTestsFromTestCase(TestVectorRepository)
        test_result = unittest.TextTestRunner().run(test_suite)
        if test_result.wasSuccessful():
            print("All tests passed!")
        else:
            print("Some tests failed.")

    def Run_tests(self):
        tests = unittest.TestLoader().loadTestsFromTestCase(TestMyVector)
        test_result = unittest.TextTestRunner().run(tests)
        if test_result.wasSuccessful():
            print("All tests passed!")
        else:
            print("Some tests failed.")




