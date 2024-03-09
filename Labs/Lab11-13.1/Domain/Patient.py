

class Patients:
    def __init__(self, firstName: str, lastName: str, CNP: str, disease: str):
        self.id_firstName = firstName
        self.id_lastName = lastName
        self.__CNP = CNP
        self.__disease = disease


    def get_id_firstName(self):
        return self.id_firstName

    def get_id_lastName(self):
        return self.id_lastName

    def get_CNP(self):
        return self.__CNP

    def get_disease(self):
        return self.__disease


    def set_id_firstName(self, id_firstName):
        self.id_firstName = id_firstName

    def set_id_lastName(self, id_lastName):
        self.id_lastName = id_lastName

    def set_CNP(self, CNP):
        self.__CNP = CNP

    def set_disease(self, disease):
        self.__disease = disease

    def __str__(self):
        return "First Name: " + self.id_firstName + "\n" + "Last Name :" + self.id_lastName + "\n" + "CNP:" + str(self.__CNP) + "\n" + "Disease: " + self.__disease

    def __repr__(self):
        return str(self)