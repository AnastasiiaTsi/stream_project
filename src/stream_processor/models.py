from typing import NamedTuple

class EmployeeRecord(NamedTuple):
    employee_id: int
    name: str
    position: str
    department: str
    salary: float