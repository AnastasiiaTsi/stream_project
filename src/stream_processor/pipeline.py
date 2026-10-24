from pathlib import Path
from collections.abc import Iterator
from stream_processor.filters import filter_by_department, filter_by_salary, validate_employees
from stream_processor.parsers import parse_csv_rows
from stream_processor.readers import read_lines
from stream_processor.transformations import normalize_names
from stream_processor.models import EmployeeRecord

def build_pipeline(
    path: Path,
    department: str | None = None,
    minimum_salary: float | None = None,
) -> Iterator[EmployeeRecord]:
    lines = read_lines(path)
    rows = parse_csv_rows(lines)
    valid = validate_employees(rows)
    normalized = normalize_names(valid)
    
    result = normalized
    if department:
        result = filter_by_department(result, department)
    if minimum_salary is not None:
        result = filter_by_salary(result, minimum_salary)
    return result