from Domain.My_Vector import MyVector
from matplotlib import pyplot as plt

class VectorRepository:
    def __init__(self):
        """Initialize an empty list"""
        self.__data = []
    def __len__(self):
        return len(self.__data)

    def getAllVectors(self):
        """Get all vectors from the repository.
        return: A list of all vectors in the repository.
        """
        return self.__data[:]

    def addVector(self, vector):
        """Add a vector to the repository.

        Args:
            vector (MyVector): The vector to be added.
        """
        self.__data.append(vector)

    def returnVectorAtIndex(self, index):
        """Get the vector at a specific index in the repository.

        Args:
            index (int): Index of the vector.
        """
        return self.__data[index]

    def updateVectorAtindex(self, index, Ni, Nc, Nt, Nv):
        """Update the attributes of a vector at a specific index.

        Args:
            index (int): Index of the vector to be updated.
            Ni: New name_id value.
            Nc: New color value.
            Nt: New type value.
            Nv: New value list.
        """
        self.__data[index].set_name_id(Ni)
        self.__data[index].set_color(Nc)
        self.__data[index].set_type(Nt)
        self.__data[index].set_value(Nv)

    def updateVectorByName_id(self, Ni, Nc, Nt, Nv):
        """Update the attributes of a vector by its name_id.

        Args:
            Ni: Name_id of the vector to be updated.
            Nc: New color value.
            Nt: New type value.
            Nv: New value list.
        """
        for elem in self.__data:
            if elem.get_name_id() == Ni:
                elem.set_color(Nc)
                elem.set_type(Nt)
                elem.set_value(Nv)

    def deleteVectorByIndex(self, Ni):
        """Delete a vector by its name_id.

        Args:
            Ni: Name_id of the vector to be deleted.
        """
        for elem in self.__data:
            if elem.get_name_id() == Ni:
                self.__data.remove(elem)

    def deleteVectorByName_id(self, Ni):
        """Delete a vector by its name_id.

        Args:
            Ni: Name_id of the vector to be deleted.
        """
        for elem in self.__data:
            if elem.get_name_id() == Ni:
                self.__data.remove(elem)

    def getSumOfVectorsWithAGivenColor(self, color):
        """Get the sum of elements for vectors with a given color.

        Args:
            color (str): The color to filter vectors.

        Returns:
                float: The sum of elements for vectors with the specified color.
        """
        result = 0
        for elem in self.__data:
            if elem.get_color() == color:
                result += elem.sum_of_elements()
        return result

    def deleteAllVectorsFromRepository(self):
        """Delete all vectors from the repository."""
        self.__data.clear()

    def updateColorByVectorName_id(self, Ni, color):
        """Update the color of a vector by its name_id.

        Args:
            Ni: Name_id of the vector to be updated.
            color: New color value.
        """
        for elem in self.__data:
            if elem.get_name_id() == Ni:
                elem.set_color(color)

    def plotVectors(self):
        """Plot vectors based on their type and color.

                The function uses Matplotlib to create a scatter plot where the x-axis represents
                the vector type and the y-axis represents the vector color. Each vector is represented
                by a marker and color based on its type and color attributes.

                The legend in the plot displays the vector ID for each point.
        """
        colors = {'r': 'red', 'g': 'green', 'b': 'blue', 'y': 'yellow', 'm': 'magenta'}
        markers = {1: 'o', 2: 's', 3: '^'}

        for vector in self.__data:
            x = vector.get_type()
            y = vector.get_color()

            if x in markers:  # Check if type is 1, 2, or 3
                marker = markers[x]  # Use the predefined marker
            else:
                marker = 'D'  # Default marker for other types

            color = colors.get(y, 'black')  # Default color for unknown colors

            plt.scatter(x, y, marker=marker, color=color, label=f"ID: {vector.get_name_id()}")

        # Set labels and legend
        plt.xlabel('Type')
        plt.ylabel('Color')
        plt.legend()

        # Show the plot
        plt.show()





