from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) <= 1:
        return container

    pivot_index = len(container) // 2
    pivot_value = container[pivot_index]

    return (
            sort([v for v in container if v < pivot_value]) +
            [v for v in container if v == pivot_value] +
            sort([v for v in container if v > pivot_value])
    )
