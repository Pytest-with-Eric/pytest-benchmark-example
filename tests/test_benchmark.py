import pytest

from src.math_examples import calculate_sum
from src.sorting_examples import bubble_sort


@pytest.mark.math
def test_calculate_sum_small(input_data_small, benchmark):
    result = benchmark(calculate_sum, input_data_small)
    assert result == sum(input_data_small)


@pytest.mark.math
def test_calculate_sum_large(input_data_large, benchmark):
    result = benchmark(calculate_sum, input_data_large)
    assert result == sum(input_data_large)


@pytest.mark.sorting
def test_bubble_sort_small(bubble_sort_input1, benchmark):
    result = benchmark(bubble_sort, bubble_sort_input1)
    assert result == sorted(bubble_sort_input1)


# Write more sorting algorithms and test/benchmark them here.
