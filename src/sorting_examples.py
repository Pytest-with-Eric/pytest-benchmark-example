def bubble_sort(input_list: list[int]):
    """
    Bubble sort algorithm.

    Args:
        input_list (list[int]): A list of numbers.

    Returns:
        list[int]: The sorted list.
    """
    indexing_length = len(input_list) - 1  # Length of list - 1
    sorted = False  # Create variable of sorted and set it equal to false

    while not sorted:
        sorted = True  # Break the while loop if sorted = True

        for i in range(0, indexing_length):  # For every value in the list
            if (
                input_list[i] > input_list[i + 1]
            ):  # If the value we are on is greater than the next value
                sorted = False  # Then the list is not sorted
                input_list[i], input_list[i + 1] = (
                    input_list[i + 1],
                    input_list[i],
                )  # Swap the values
    return input_list  # Return the sorted list
