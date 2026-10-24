from collections import Counter
from collections.abc import Iterable
from stream_processor.models import EmployeeRecord

def calculate_statistics(employees: Iterable[EmployeeRecord]) -> dict:
    count = 0
    total_salary = 0.0
    maximum = None
    best_employee = None
    departments = Counter()

    for employee in employees:
        count += 1
        total_salary += employee.salary
        departments[employee.department] += 1
        if maximum is None or employee.salary > maximum:
            maximum = employee.salary
            best_employee = employee

    average = total_salary / count if count else 0.0
    return {
        "count": count,
        "average": average,
        "total_payroll": total_salary,
        "max_salary": maximum,
        "best_employee": best_employee,
        "departments": dict(departments),
    }