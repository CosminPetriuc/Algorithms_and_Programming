import unittest
from Repo.PatientRepo import PatientsRepository
from Repo.DepartmentRepo import DepartmentsRepository
from Domain.Patient import Patients
from Domain.Departments import Departament

class TestRepo(unittest.TestCase):
    def setUp(self):
        self.patients_repository = PatientsRepository()
        self.departments_repository = DepartmentsRepository()

        self.sample_department1 = Departament(1, "Internal Medicine", 20, [])
        self.sample_department2 = Departament(2, "Pediatrics", 15, [])

        self.sample_patient1 = Patients("John", "Doe", "9501011234567", "Fever")
        self.sample_patient2 = Patients("Jane", "Smith", "9802022345678", "Headache")

        # Test methods for PatientsRepository

    def test_add_patient(self):
        self.patients_repository.add_patient(self.sample_patient1)
        self.assertEqual(len(self.patients_repository.get_all_patients()), 1)

    def test_get_patient_by_cnp(self):
        self.patients_repository.add_patient(self.sample_patient1)
        self.patients_repository.add_patient(self.sample_patient2)
        retrieved_patient = self.patients_repository.get_patient_by_cnp("9802022345678")
        self.assertEqual(retrieved_patient, self.sample_patient2)

    def test_update_patient(self):
        self.patients_repository.add_patient(self.sample_patient1)
        updated_patient = Patients("John", "Doe", "9501011234567", "Updated Disease")
        self.patients_repository.update_patient("9501011234567", updated_patient)
        retrieved_patient = self.patients_repository.get_patient_by_cnp("9501011234567")
        self.assertEqual(retrieved_patient.get_disease(), "Updated Disease")

    def test_delete_patient(self):
        self.patients_repository.add_patient(self.sample_patient1)
        self.patients_repository.add_patient(self.sample_patient2)
        self.patients_repository.delete_patient("9501011234567")
        self.assertEqual(len(self.patients_repository.get_all_patients()), 1)

    def test_get_all_patients(self):
        self.patients_repository.add_patient(self.sample_patient1)
        self.patients_repository.add_patient(self.sample_patient2)
        all_patients = self.patients_repository.get_all_patients()
        self.assertEqual(len(all_patients), 2)

        # Test methods for DepartmentsRepository

    def test_add_department(self):
        self.departments_repository.add_department(self.sample_department1)
        self.assertEqual(len(self.departments_repository.get_all_departments()), 1)

    def test_get_department_by_id(self):
        self.departments_repository.add_department(self.sample_department1)
        self.departments_repository.add_department(self.sample_department2)
        retrieved_department = self.departments_repository.get_department_by_id(2)
        self.assertEqual(retrieved_department, self.sample_department2)

    def test_update_department(self):
        self.departments_repository.add_department(self.sample_department1)
        updated_department = Departament(1, "Internal Medicine Updated", 25, [])
        self.departments_repository.update_department(1, updated_department)
        retrieved_department = self.departments_repository.get_department_by_id(1)
        self.assertEqual(retrieved_department.get_name(), "Internal Medicine Updated")

    def test_delete_department(self):
        self.departments_repository.add_department(self.sample_department1)
        self.departments_repository.add_department(self.sample_department2)
        self.departments_repository.delete_department(1)
        self.assertEqual(len(self.departments_repository.get_all_departments()), 1)

    def test_get_all_departments(self):
        self.departments_repository.add_department(self.sample_department1)
        self.departments_repository.add_department(self.sample_department2)
        all_departments = self.departments_repository.get_all_departments()
        self.assertEqual(len(all_departments), 2)
