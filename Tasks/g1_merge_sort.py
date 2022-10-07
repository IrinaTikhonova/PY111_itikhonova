from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) == 1:
        return container

    final_result = []
    middle = len(container)//2

    while container[0:middle] or container[middle:-1]:
        sort(container[0:middle])




    return container
