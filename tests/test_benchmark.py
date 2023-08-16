import pytest
from src.math_examples import calculate_sum
from src.sorting_examples import bubble_sort, quick_sort, insertion_sort


@pytest.mark.math_small
def test_calculate_sum_small(input_data_small, benchmark):
    result = benchmark(calculate_sum, input_data_small)
    assert result == sum(input_data_small)


@pytest.mark.math_small
def test_inbuilt_sum_small(input_data_small, benchmark):
    result = benchmark(sum, input_data_small)
    assert result == sum(input_data_small)


@pytest.mark.math_large
def test_calculate_sum_large(input_data_large, benchmark):
    result = benchmark(calculate_sum, input_data_large)
    assert result == sum(input_data_large)


@pytest.mark.math_large
def test_inbuilt_sum_large(input_data_large, benchmark):
    result = benchmark(sum, input_data_large)
    assert result == sum(input_data_large)


# Sorting - Small
@pytest.mark.sort_small
def test_bubble_sort_small(sort_input1, benchmark):
    result = benchmark(bubble_sort, sort_input1)
    assert result == sorted(sort_input1)


@pytest.mark.sort_small
def test_quick_sort_small(sort_input1, benchmark):
    result = benchmark(quick_sort, sort_input1)
    assert result == sorted(sort_input1)


@pytest.mark.sort_small
def test_insertion_sort_small(sort_input1, benchmark):
    result = benchmark(insertion_sort, sort_input1)
    assert result == sorted(sort_input1)


@pytest.mark.sort_small
def test_inbuilt_sort_small(sort_input1, benchmark):
    result = benchmark(sorted, sort_input1)
    assert result == sorted(sort_input1)


# Sorting - Large
@pytest.mark.sort_large
def test_bubble_sort_large(sort_input2, benchmark):
    result = benchmark(bubble_sort, sort_input2)
    assert result == sorted(sort_input2)


@pytest.mark.sort_large
def test_quick_sort_large(sort_input2, benchmark):
    result = benchmark(quick_sort, sort_input2)
    assert result == sorted(sort_input2)


@pytest.mark.sort_large
def test_inbuilt_sort_large(sort_input2, benchmark):
    result = benchmark(sorted, sort_input2)
    assert result == sorted(sort_input2)


@pytest.mark.sort_large
def test_insertion_sort_large(sort_input2, benchmark):
    result = benchmark(insertion_sort, sort_input2)
    assert result == sorted(sort_input2)
