from itertools import islice
from pathlib import Path
from stream_processor.analytics import calculate_statistics
from stream_processor.pipeline import build_pipeline
from stream_processor.batches import batched_employees

def main() -> None:
    path = Path("data/employees.csv")

    pipeline = build_pipeline(path, minimum_salary=20000.0)
    print("First 3 employees with salary >= 20000:")
    for employee in islice(pipeline, 3):
        print(f"  {employee.employee_id}, {employee.name}, {employee.salary}")

    pipeline = build_pipeline(path, department="IT")
    stats = calculate_statistics(pipeline)
    print("\nStatistics for IT department:")
    for key, value in stats.items():
        print(f"  {key}: {value}")

    pipeline = build_pipeline(path)
    print("\nBatch export (size=2):")
    for i, batch in enumerate(batched_employees(pipeline, 2), 1):
        print(f"  Batch {i}: {[e.name for e in batch]}")

if __name__ == "__main__":
    main()