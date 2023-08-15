import pytest


@pytest.fixture
def input_data_small():
    return list(range(100))


@pytest.fixture
def input_data_large():
    return list(range(10000))


@pytest.fixture
def bubble_sort_input1():
    return [5, 1, 4, 2, 8, 9, 3, 7, 6, 0]
