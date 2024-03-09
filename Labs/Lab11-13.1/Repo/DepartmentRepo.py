from Domain.Departments import Departament


class DepartmentsRepository:
    def __init__(self):
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def get_department_by_id(self, department_id):
        return next((department for department in self.departments if department.get_id() == department_id), None)

    def update_department(self, department_id, updated_department):
        for i, department in enumerate(self.departments):
            if department.get_id() == department_id:
                self.departments[i] = updated_department
                break

    def delete_department(self, department_id):
        self.departments = [department for department in self.departments if department.get_id() != department_id]

    def get_all_departments(self):
        return self.departments
