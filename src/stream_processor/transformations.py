from collections.abc import Iterable, Iterator
from stream_processor.models import EmployeeRecord

def normalize_names(employees: Iterable[EmployeeRecord]) -> Iterator[EmployeeRecord]:
    for employee in employees:
        yield employee._replace(name=employee.name.title())