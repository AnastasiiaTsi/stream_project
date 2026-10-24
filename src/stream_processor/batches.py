from collections.abc import Iterable, Iterator
from itertools import islice
from stream_processor.models import EmployeeRecord

def batched_employees(
    employees: Iterable[EmployeeRecord], batch_size: int
) -> Iterator[list[EmployeeRecord]]:
    iterator = iter(employees)
    while True:
        batch = list(islice(iterator, batch_size))
        if not batch:
            return
        yield batch