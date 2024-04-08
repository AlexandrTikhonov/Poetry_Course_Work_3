from src.utils import getting_file, filtration_list, sorted_date, get_date, get_num, get_sum, get_main
import os
from config import ROOT_DIR


def test_getting_file():
    test_path = os.path.join(ROOT_DIR, 'tests', 'test_operations.json')
    assert getting_file(test_path) != []
