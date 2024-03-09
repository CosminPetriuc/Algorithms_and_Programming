from UI.UI import UI
from Service.Service import HospitalService
from Repo.PatientRepo import PatientsRepository
from Repo.DepartmentRepo import DepartmentsRepository
from Domain.Patient import Patients
from Domain.Departments import Departament

def main():
    patients_repo = PatientsRepository()
    departments_repo = DepartmentsRepository()
    hospital_service = HospitalService(patients_repo, departments_repo)

    patient1 = Patients("John", "Doe", "9501011234567", "Fever")
    patient2 = Patients("Jane", "Smith", "9802022345678", "Headache")
    patient3 = Patients("Alice", "Johnson", "9903033456789", "Cough")

    department1 = Departament(1, "Cardio", 20, [patient1, patient2])
    department2 = Departament(2, "Pediatrics", 15, [patient3])

    patients_repo.add_patient(patient1)
    patients_repo.add_patient(patient2)
    patients_repo.add_patient(patient3)

    departments_repo.add_department(department1)
    departments_repo.add_department(department2)

    ui = UI(hospital_service)
    ui.run()


if __name__ == "__main__":
    main()