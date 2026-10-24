from pathlib import Path
from stream_processor.pipeline import build_pipeline
from stream_processor.filters import filter_by_salary
from stream_processor.models import EmployeeRecord


def test_pipeline(tmp_path: Path):
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(
        "employee_id,name,position,department,salary\n"
        "1,anna koval,Developer,IT,25000\n"
        "2,invalid,Unknown,IT,error\n"
        "3,iryna bondar,Manager,Management,30000\n"
    )
    result = list(build_pipeline(csv_file))
    assert len(result) == 2
    assert result[0].name == "Anna Koval"
    assert result[1].department == "Management"


def test_filter_by_salary():
    employees = [
        EmployeeRecord(1, "A", "Dev", "IT", 100.0),
        EmployeeRecord(2, "B", "Dev", "IT", 200.0),
    ]
    filtered = list(filter_by_salary(employees, 150.0))
    assert len(filtered) == 1
    assert filtered[0].employee_id == 2