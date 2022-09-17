def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError(f"Is there a {n} number of Fibonacci sequence? I think here should be an exception...")
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError(f"Is there a {n} number of Fibonacci sequence? I think here should be and exception...")

    if n == 1 or n == 2:
        return 1

    elif n > 2:
        num_1 = 1
        num_2 = 1
        for _ in range(3, n+1):
            mid_result = num_1 + num_2
            num_1, num_2 = num_2, mid_result

        return mid_result
