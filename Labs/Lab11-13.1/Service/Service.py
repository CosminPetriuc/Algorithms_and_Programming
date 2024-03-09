from Repo.PatientRepo import PatientsRepository
from Repo.DepartmentRepo import DepartmentsRepository
from datetime import datetime



class HospitalService:
    """
        HospitalService class represents the service layer for managing patients and departments in a hospital.

        Attributes:
            patients_repo (PatientsRepository): The repository for managing patient data.
            departments_repo (DepartmentsRepository): The repository for managing department data.
        """
    def __init__(self, patients_repo, departments_repo):
        """
                Initialize a new instance of HospitalService.

                Parameters:
                    patients_repo (PatientsRepository): The repository for managing patient data.
                    departments_repo (DepartmentsRepository): The repository for managing department data.
                """
        self.patients_repo = patients_repo
        self.departments_repo = departments_repo

    # Patients CRUD operations
    def add_patient_to_department(self, patient, department_id):
        """
                Add a patient to a specific department.

                Parameters:
                    patient (Patients): The patient to be added.
                    department_id (int): The ID of the department to which the patient should be added.
                """
        department = self.departments_repo.get_department_by_id(department_id)
        if department:
            department.get_pacient_list().append(patient)
            self.departments_repo.update_department(department_id, department)

    def add_patient(self, patient):
        """
               Add a patient to the hospital. Prompt the user to specify the department for the patient.

               Parameters:
                   patient (Patients): The patient to be added.
               """
        self.patients_repo.add_patient(patient)
        department_id = int(input("Enter the department ID to add the patient to: "))
        self.add_patient_to_department(patient, department_id)
        print("Patient added to the specified department successfully!")

    def get_patient_by_cnp(self, cnp):
        """
               Retrieve a patient by their CNP (Personal Identification Number).

               Parameters:
                   cnp (str): The CNP of the patient.

               Returns:
                   Patients: The patient with the specified CNP, or None if not found.
               """
        return self.patients_repo.get_patient_by_cnp(cnp)

    def update_patient(self, cnp, updated_patient):
        """
               Update patient information.

               Parameters:
                   cnp (str): The CNP of the patient to be updated.
                   updated_patient (Patients): The updated patient information.
               """
        self.patients_repo.update_patient(cnp, updated_patient)

    def delete_patient(self, cnp):
        """
               Delete a patient by their CNP.

               Parameters:
                   cnp (str): The CNP of the patient to be deleted.
               """
        self.patients_repo.delete_patient(cnp)

    def get_all_patients(self):
        """
               Retrieve a list of all patients in the hospital.

               Returns:
                   list: A list of Patients objects representing all patients in the hospital.
               """
        return self.patients_repo.get_all_patients()

    # Departments CRUD operations
    def add_department(self, department):
        """
               Add a new department.

               Parameters:
                   department (Departament): The department to be added.
               """
        self.departments_repo.add_department(department)

    def get_department_by_id(self, department_id):
        """
               Retrieve a department by its ID.

               Parameters:
                   department_id (int): The ID of the department.

               Returns:
                   Departament: The department with the specified ID, or None if not found.
               """
        return self.departments_repo.get_department_by_id(department_id)

    def update_department(self, department_id, updated_department):
        """
              Update department information.

              Parameters:
                  department_id (int): The ID of the department to be updated.
                  updated_department (Departament): The updated department information.
              """
        self.departments_repo.update_department(department_id, updated_department)

    def delete_department(self, department_id):
        """
               Delete a department by its ID.

               Parameters:
                   department_id (int): The ID of the department to be deleted.
               """
        self.departments_repo.delete_department(department_id)

    def get_all_departments(self):
        """
               Retrieve a list of all departments in the hospital.

               Returns:
                   list: A list of Departament objects representing all departments in the hospital.
               """
        return self.departments_repo.get_all_departments()

    def sort_patients_in_department_by_cnp(self, department_id):
        """
                Sort patients in a specific department by their CNP.

                Parameters:
                    department_id (int): The ID of the department.

                Returns:
                    list: A list of Patients objects representing patients in the specified department, sorted by CNP.
                """
        patients = self.patients_repo.sort_patients_by_cnp_in_department(department_id)
        return patients

    def sort_departments_by_number_of_patients(self):
        """
              Sort departments by the number of patients they have.

              Returns:
                  list: A list of Departament objects representing departments, sorted by the number of patients.
              """
        departments = self.departments_repo.get_all_departments()
        departments.sort(key=lambda department: len(department.get_pacient_list()))
        return departments

    def sort_departments_by_number_of_patients_above_age(self, age_limit):
        """
               Sort departments by the number of patients above a specified age.

               Parameters:
                   age_limit (int): The age limit.

               Returns:
                   list: A list of Departament objects representing departments, sorted by the number of patients above the age limit.
               """
        departments = self.departments_repo.get_all_departments()
        departments.sort(
            key=lambda department: sum(
                1 for patient in department.get_pacient_list() if self.calculate_age_from_cnp(patient.get_CNP()) > age_limit
            )
        )
        return departments

    def sort_departments_by_number_of_patients_alphabetically(self):
        """
               Sort departments alphabetically by their names.

               Returns:
                   list: A list of Departament objects representing departments, sorted alphabetically.
               """
        departments = self.departments_repo.get_all_departments()
        departments.sort(key=lambda department: (len(department.get_pacient_list()), str(department)))
        return departments

    def identify_departments_with_patients_below_age(self, age_limit):
        """
               Identify departments with patients below a specified age.

               Parameters:
                   age_limit (int): The age limit.

               Returns:
                   list: A list of Departament objects representing departments with patients below the age limit.
               """
        departments = self.departments_repo.get_all_departments()
        return [department for department in departments if any(
            self.calculate_age_from_cnp(patient.get_CNP()) < age_limit for patient in department.get_pacient_list()
        )]

    def identify_patients_by_name(self, search_string):
        """
               Identify patients by their names or part of their names.

               Parameters:
                   search_string (str): The name or part of the name to search for.

               Returns:
                   list: A list of Patients objects representing patients with names matching the search string.
               """
        return self.patients_repo.identify_patients_by_name(search_string)


    def calculate_age_from_cnp(self, cnp):
        """
               Calculate the age of a person based on their CNP (Personal Identification Number).

               Parameters:
                   cnp (str): The CNP of the person.

               Returns:
                   int: The calculated age.
               """
        birthdate_str = cnp[:6]
        birthdate = datetime.strptime(birthdate_str, '%y%m%d')

        current_date = datetime.now()
        age = current_date.year - birthdate.year - (
                    (current_date.month, current_date.day) < (birthdate.month, birthdate.day))

        return age

    def identify_departments_with_patients_by_first_name(self, first_name):
        """
        Identify departments with patients having a given first name.

        Parameters:
            first_name (str): The first name to search for.

        Returns:
            list: A list of Departament objects representing departments with patients having the given first name.
        """
        departments = self.departments_repo.get_all_departments()
        result_departments = []

        for department in departments:
            patients_with_first_name = any(
                patient.get_id_firstName().lower() == first_name.lower() for patient in department.get_pacient_list()
            )

            if patients_with_first_name:
                result_departments.append(department)

        return result_departments