import numpy as np

class MyVector():
    def __init__(self, id, color, type, *value):
        c = ['r', 'g', 'b', 'y', 'm']
        self.__name_id = id
        self.__value = np.array(value)
        self.__color = color
        self.__type = type


    def get_name_id(self):
        return self.__name_id

    def get_color(self):
        return self.__color

    def get_type(self):
        return self.__type

    def get_value(self):
        return self.__value

    def set_name_id(self, new_name_id):
        self.__name_id = new_name_id

    def set_color(self, new_c):
        self.__color = new_c

    def set_type(self, new_type):
        self.__type = new_type

    def set_value(self, new_value):
        self.__value = np.array(new_value)

    def __str__(self):
        return f"Vector ID is: {self.__name_id} with the color: {self.__color}, type: {self.__type} and the value: {self.__value.tolist()}"

    def add_scalar_to_vector(self, scalar):
        self.__value += scalar

    def add_two_vectors(self, vector):
        if len(self.__value) != len(vector.get_value()):
            raise ValueError("The two vectors must have the same length")
        self.__value += np.array(vector.get_value())

    def subtract_two_vectors(self, vector):
        if len(self.__value) != len(vector.get_value()):
            raise ValueError("The two vectors must have the same length")
        self.__value -= np.array(vector.get_value())

    def multiply_two_vectors(self, vector):
        if len(self.__value) != len(vector.get_value()):
            raise ValueError("The two vectors must have the same length")
        self.__value *= np.array(vector.get_value())

    def sum_of_elements(self):
        return np.sum(self.__value)

    def product_of_elements(self):
        return np.prod(self.__value)

    def average_of_elements(self):
        return np.mean(self.__value)

    def min_of_vector(self):
        return np.min(self.__value)

    def max_of_vector(self):
        return np.max(self.__value)
