def calculate_sum(numbers: list[int]):
    """
    Calculate the sum of a list of numbers.

    Args:
        numbers (list[int]): A list of numbers.

    Returns:
        int: The sum of the numbers.
    """
    total = 0
    for num in numbers:
        total += num
    return total
