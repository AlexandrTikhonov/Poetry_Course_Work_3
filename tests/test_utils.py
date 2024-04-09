import pytest
from src.utils import getting_file, filtration_list, sorted_date, get_date, get_num, get_sum, get_main
import os
from config import ROOT_DIR

operations = [
    {"id": 1, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000000"},
    {"id": 2, "state": "EXECUTED", "date": "2018-02-01T00:00:00.000000"},
    {"id": 3, "state": "EXECUTED", "date": "2018-03-01T00:00:00.000000"},
    {"id": 4, "state": "EXECUTED", "date": "2018-04-01T00:00:00.000000"}
]


@pytest.fixture
def operations_fixture():
    return operations


test_path = os.path.join(ROOT_DIR, 'tests', 'test_operations.json')


def test_getting_file():
    assert getting_file(test_path) != []


def test_filtration_list(operations_fixture):
    assert len(filtration_list(operations_fixture)) == 4


def test_sorted_date(operations_fixture):
    assert [i["id"] for i in sorted_date(operations_fixture)] == [4, 3, 2, 1]
