from Domain.Departments import Departament
from Domain.Patient import Patients
from Repo.DepartmentRepo import DepartmentsRepository
from Repo.PatientRepo import PatientsRepository
from datetime import datetime
from Service.Service import HospitalService

patients_repo = PatientsRepository()
departments_repo = DepartmentsRepository()
hospital_service = HospitalService(patients_repo, departments_repo)

patient1 = Patients("John", "Doe", "9501011234567", "Fever")
patient2 = Patients("Jane", "Smith", "9802022345678", "Headache")
patient3 = Patients("Alice", "Johnson", "9903033456789", "Cough")

department1 = Departament(1, "Internal Medicine", 20, [patient1, patient2])
department2 = Departament(2, "Pediatrics", 15, [patient3])


patients_repo.add_patient(patient1)
patients_repo.add_patient(patient2)
patients_repo.add_patient(patient3)

departments_repo.add_department(department1)
departments_repo.add_department(department2)

class UI:
    def __init__(self, hospital_service):
        self.hospital_service = hospital_service

    def print_menu(self):
        print("1. Add Patient")
        print("2. Add Department")
        print("3. List All Patients")
        print("4. List All Departments")
        print("5. Sort Patients in a Department by CNP")
        print("6. Sort Departments by Number of Patients")
        print("7. Sort Departments by Number of Patients Above Age")
        print("8. Sort Departments Alphabetically")
        print("9. Identify Departments with Patients Below Age")
        print("10. Identify Patients by Name")
        print("11. Update Patient Information")
        print("12. Identify Patients By First Name")
        print("0. Exit")

    def run(self):
        while True:
            self.print_menu()
            choice = input("Enter your choice (0 to exit): ")

            if choice == "0":
                print("Exiting the application. Goodbye!")
                break
            elif choice == "1":
                self.add_patient()
            elif choice == "2":
                self.add_department()
            elif choice == "3":
                self.list_all_patients()
            elif choice == "4":
                self.list_all_departments()
            elif choice == "5":
                self.sort_patients_in_department_by_cnp()
            elif choice == "6":
                self.sort_departments_by_number_of_patients()
            elif choice == "7":
                self.sort_departments_by_number_of_patients_above_age()
            elif choice == "8":
                self.sort_departments_alphabetically()
            elif choice == "9":
                self.identify_departments_with_patients_below_age()
            elif choice == "10":
                self.identify_patients_by_name()
            elif choice == "11":
                self.update_patient()
            elif choice == "12":
                self.identify_departments_with_patients_by_first_name()

            input("Press Enter to continue...")

    def add_patient(self):
        first_name = input("Enter patient's first name: ")
        last_name = input("Enter patient's last name: ")
        cnp = input("Enter patient's CNP: ")
        disease = input("Enter patient's disease: ")

        patient = Patients(first_name, last_name, cnp, disease)
        self.hospital_service.add_patient(patient)
        print("Patient added successfully!")

        # Prompt to associate the patient with a department
        associate_department = input("Do you want to associate this patient with a department? (y/n): ").lower()
        if associate_department == 'y':
            self.associate_patient_with_department(patient)

    def associate_patient_with_department(self, patient):
        try:
            department_id = int(input("Enter the department ID to associate the patient with: "))
            self.hospital_service.add_patient_to_department(patient, department_id)
            print("Patient associated with the specified department successfully!")
        except ValueError:
            print("Invalid input. Please enter a valid integer for the department ID.")

    def add_department(self):
        try:
            department_id = int(input("Enter department ID: "))
            department_name = input("Enter department name: ")
            number_of_beds = int(input("Enter number of beds: "))
            patients = []
            department = Departament(department_id, department_name, number_of_beds, patients)
            self.hospital_service.add_department(department)
            print("Department added successfully!")
        except ValueError:
            print("Invalid input. Please enter a valid integer for the department ID and number of beds.")

    def list_all_patients(self):
        patients = self.hospital_service.get_all_patients()
        if patients:
            for patient in patients:
                print(patient)
        else:
            print("No patients found.")

    def list_all_departments(self):
        departments = self.hospital_service.get_all_departments()
        if departments:
            for department in departments:
                print(department)
        else:
            print("No departments found.")

    def sort_patients_in_department_by_cnp(self):
        try:
            department_id = int(input("Enter department ID to sort patients: "))
            patients = self.hospital_service.sort_patients_in_department_by_cnp(department_id)
            if patients:
                for patient in patients:
                    print(patient)
            else:
                print("No patients found in the specified department.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for the department ID.")

    def sort_departments_by_number_of_patients(self):
        departments = self.hospital_service.sort_departments_by_number_of_patients()
        if departments:
            for department in departments:
                print(department)
        else:
            print("No departments found.")

    def sort_departments_by_number_of_patients_above_age(self):
        try:
            age_limit = int(input("Enter the age limit: "))
            departments = self.hospital_service.sort_departments_by_number_of_patients_above_age(age_limit)
            if departments:
                for department in departments:
                    print(department)
            else:
                print("No departments found.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for the age limit.")

    def sort_departments_alphabetically(self):
        departments = self.hospital_service.sort_departments_by_number_of_patients_alphabetically()
        if departments:
            for department in departments:
                print(department)
        else:
            print("No departments found.")

    def identify_departments_with_patients_below_age(self):
        try:
            age_limit = int(input("Enter the age limit: "))
            departments = self.hospital_service.identify_departments_with_patients_below_age(age_limit)
            if departments:
                for department in departments:
                    print(department)
            else:
                print("No departments found.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for the age limit.")

    def identify_patients_by_name(self):
        search_string = input("Enter the name or part of the name to search: ")
        patients = self.hospital_service.identify_patients_by_name(search_string)
        if patients:
            for patient in patients:
                print(patient)
        else:
            print("No patients found.")

    def update_patient(self):
        cnp = input("Enter patient's CNP to update: ")
        updated_first_name = input("Enter updated first name (leave empty to keep current): ")
        updated_last_name = input("Enter updated last name (leave empty to keep current): ")
        updated_disease = input("Enter updated disease (leave empty to keep current): ")

        existing_patient = self.hospital_service.get_patient_by_cnp(cnp)

        if existing_patient:
            updated_patient = Patients(
                updated_first_name or existing_patient.get_id_firstName(),
                updated_last_name or existing_patient.get_id_lastName(),
                cnp,
                updated_disease or existing_patient.get_disease()
            )
            self.hospital_service.update_patient(cnp, updated_patient)
            print("Patient updated successfully!")
        else:
            print("Patient not found.")

    def identify_departments_with_patients_by_first_name(self):
        first_name = input("Enter the first name to search for: ")
        departments = self.hospital_service.identify_departments_with_patients_by_first_name(first_name)

        if departments:
            print(f"Departments with patients having the first name '{first_name}':")
            for department in departments:
                print(department)
        else:
            print(f"No departments found with patients having the first name '{first_name}'.")