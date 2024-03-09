from Domain.Patient import Patients

class PatientsRepository:
    def __init__(self):
        self.patients = []


    def add_patient(self, patient):
        self.patients.append(patient)

    def get_patient_by_cnp(self, cnp):
        return next((patient for patient in self.patients if patient.get_CNP() == cnp), None)

    def update_patient(self, cnp, updated_patient):
        for i, patient in enumerate(self.patients):
            if patient.get_CNP() == cnp:
                self.patients[i] = updated_patient
                break

    def delete_patient(self, cnp):
        self.patients = [patient for patient in self.patients if patient.get_CNP() != cnp]

    def get_all_patients(self):
        return self.patients

    def sort_patients_by_cnp_in_department(self, department_id):
        patients_in_department = [patient for patient in self.patients if patient.get_department_id() == department_id]
        patients_in_department.sort(key=lambda patient: patient.get_CNP())
        return patients_in_department

    def identify_patients_by_name(self, search_string):
        return [patient for patient in self.patients if
                search_string.lower() in patient.get_id_firstName().lower() or
                search_string.lower() in patient.get_id_lastName().lower()]

