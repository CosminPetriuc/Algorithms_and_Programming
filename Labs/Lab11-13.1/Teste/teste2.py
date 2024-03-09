import unittest
from Domain.Departments import  Departament
from Domain.Patient import Patients
from Repo.DepartmentRepo import DepartmentsRepository
from Repo.PatientRepo import PatientsRepository
from Service.Service import HospitalService

class TestHospitalService(unittest.TestCase):
    def setUp(self):
        self.patients_repo = PatientsRepository()
        self.departments_repo = DepartmentsRepository()
        self.hospital_service = HospitalService(self.patients_repo, self.departments_repo)

        self.sample_patient1 = Patients("John", "Doe", "9501011234567", "Fever")
        self.sample_patient2 = Patients("Jane", "Smith", "9802022345678", "Headache")

        self.sample_department1 = Departament(1, "Internal Medicine", 20, [self.sample_patient1, self.sample_patient2])
        self.sample_department2 = Departament(2, "Pediatrics", 15, [])

    def test_add_patient_to_department(self):
        self.hospital_service.add_department(self.sample_department1)
        self.hospital_service.add_patient_to_department(self.sample_patient2, 1)
        self.assertEqual(len(self.sample_department1.get_pacient_list()), 2)

    def test_add_patient(self):
        self.hospital_service.add_patient(self.sample_patient1)
        self.assertEqual(len(self.hospital_service.get_all_patients()), 1)

    def test_get_patient_by_cnp(self):
        self.hospital_service.add_patient(self.sample_patient1)
        retrieved_patient = self.hospital_service.get_patient_by_cnp("9501011234567")
        self.assertEqual(retrieved_patient, self.sample_patient1)

    def test_update_patient(self):
        self.hospital_service.add_patient(self.sample_patient1)
        updated_patient = Patients("John", "Doe", "9501011234567", "Updated Disease")
        self.hospital_service.update_patient("9501011234567", updated_patient)
        retrieved_patient = self.hospital_service.get_patient_by_cnp("9501011234567")
        self.assertEqual(retrieved_patient.get_disease(), "Updated Disease")

    def test_delete_patient(self):
        self.hospital_service.add_patient(self.sample_patient1)
        self.hospital_service.delete_patient("9501011234567")
        self.assertEqual(len(self.hospital_service.get_all_patients()), 0)

    def test_get_all_patients(self):
        self.hospital_service.add_patient(self.sample_patient1)
        self.hospital_service.add_patient(self.sample_patient2)
        all_patients = self.hospital_service.get_all_patients()
        self.assertEqual(len(all_patients), 2)

    def test_add_department(self):
        self.hospital_service.add_department(self.sample_department1)
        self.assertEqual(len(self.hospital_service.get_all_departments()), 1)

    def test_get_department_by_id(self):
        self.hospital_service.add_department(self.sample_department1)
        retrieved_department = self.hospital_service.get_department_by_id(1)
        self.assertEqual(retrieved_department, self.sample_department1)

    def test_update_department(self):
        self.hospital_service.add_department(self.sample_department1)
        updated_department = Departament(1, "Internal Medicine Updated", 25, [])
        self.hospital_service.update_department(1, updated_department)
        retrieved_department = self.hospital_service.get_department_by_id(1)
        self.assertEqual(retrieved_department.get_name(), "Internal Medicine Updated")

    def test_delete_department(self):
        self.hospital_service.add_department(self.sample_department1)
        self.hospital_service.delete_department(1)
        self.assertEqual(len(self.hospital_service.get_all_departments()), 0)

    def test_get_all_departments(self):
        self.hospital_service.add_department(self.sample_department1)
        self.hospital_service.add_department(self.sample_department2)
        all_departments = self.hospital_service.get_all_departments()
        self.assertEqual(len(all_departments), 2)

    def test_sort_patients_in_department_by_cnp(self):
        self.hospital_service.add_department(self.sample_department1)
        patients_sorted = self.hospital_service.sort_patients_in_department_by_cnp(1)
        expected_order = sorted([self.sample_patient1, self.sample_patient2], key=lambda patient: patient.get_CNP())
        self.assertEqual(patients_sorted, expected_order)

    def test_sort_departments_by_number_of_patients(self):
        self.hospital_service.add_department(self.sample_department1)
        self.hospital_service.add_department(self.sample_department2)
        departments_sorted = self.hospital_service.sort_departments_by_number_of_patients()
        expected_order = sorted([self.sample_department1, self.sample_department2],
                                key=lambda department: len(department.get_pacient_list()))
        self.assertEqual(departments_sorted, expected_order)

    def test_sort_departments_by_number_of_patients_above_age(self):
        self.hospital_service.add_department(self.sample_department1)
        self.hospital_service.add_department(self.sample_department2)
        departments_sorted = self.hospital_service.sort_departments_by_number_of_patients_above_age(20)
        expected_order = sorted([self.sample_department1, self.sample_department2],
                                key=lambda department: sum(
                                    1 for patient in department.get_pacient_list() if
                                    self.hospital_service.calculate_age_from_cnp(patient.get_CNP()) > 20
                                ))
        self.assertEqual(departments_sorted, expected_order)

    def test_sort_departments_by_number_of_patients_alphabetically(self):
        self.hospital_service.add_department(self.sample_department2)
        self.hospital_service.add_department(self.sample_department1)
        departments_sorted = self.hospital_service.sort_departments_by_number_of_patients_alphabetically()
        expected_order = sorted([self.sample_department1, self.sample_department2],
                                key=lambda department: (len(department.get_pacient_list()), str(department)))
        self.assertEqual(departments_sorted, expected_order)

    def test_identify_departments_with_patients_below_age(self):
        self.hospital_service.add_department(self.sample_department1)
        self.hospital_service.add_department(self.sample_department2)
        departments_identified = self.hospital_service.identify_departments_with_patients_below_age(25)
        self.assertEqual(departments_identified, [self.sample_department1])

    def test_identify_patients_by_name(self):
        self.hospital_service.add_patient(self.sample_patient1)
        self.hospital_service.add_patient(self.sample_patient2)
        patients_identified = self.hospital_service.identify_patients_by_name("John")
        self.assertEqual(patients_identified, [self.sample_patient1])

    def test_calculate_age_from_cnp(self):
        age = self.hospital_service.calculate_age_from_cnp("9501011234567")
        self.assertGreaterEqual(age, 0)
