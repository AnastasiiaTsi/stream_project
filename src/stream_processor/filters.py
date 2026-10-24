from collections.abc import Iterable, Iterator
from stream_processor.models import EmployeeRecord

def validate_employees(rows: Iterable[dict[str, str]]) -> Iterator[EmployeeRecord]:
    for row in rows:
        try:
            employee_id = int(row["employee_id"])
            name = row["name"].strip()
            position = row["position"].strip()
            department = row["department"].strip()
            salary = float(row["salary"])
        except (ValueError, TypeError, KeyError):
            continue
        if not name or not department:
            continue
        if salary < 0:
            continue
        yield EmployeeRecord(employee_id, name, position, department, salary)

def filter_by_department(
    employees: Iterable[EmployeeRecord], department: str
) -> Iterator[EmployeeRecord]:
    for employee in employees:
        if employee.department == department:
            yield employee

def filter_by_salary(
    employees: Iterable[EmployeeRecord], minimum: float
) -> Iterator[EmployeeRecord]:
    for employee in employees:
        if employee.salary >= minimum:
            yield employee