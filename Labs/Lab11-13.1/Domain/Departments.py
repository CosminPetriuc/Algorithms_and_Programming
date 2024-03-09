

class Departament:
    def __init__(self, id_dep: int, name: str, beds: int, patient_list: list):
        self.__id_dep = id_dep
        self.__name = name
        self.__beds = beds
        self.__patient_list = patient_list

    def get_id(self):
        return self.__id_dep

    def get_name(self):
        return self.__name

    def get_beds(self):
        return self.__beds

    def get_pacient_list(self):
        return self.__patient_list

    def set_id_dep(self, id_dep):
        self.__id_dep = id_dep

    def set_name(self, name):
        self.__name = name

    def set_beds(self, beds):
        self.__beds = beds

    def set_pacient_list(self, patient_list):
        self.__patient_list = patient_list

    def __str__(self):
        return "Id: " + str(self.__id_dep) + "\n" + "Name :" + self.__name + "\n" + "Beds:" + str(self.__beds) + "\n" + "Patient List: " + str(self.__patient_list)

    def __repr__(self):
        return f"Departament(id: {self.__id_dep}, name: {self.__name}, beds: {self.__beds}, patients: {self.__patient_list})"