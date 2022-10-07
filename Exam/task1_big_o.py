# Оценить асимптотическую сложность приведенного ниже алгоритма:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = len(arr) - 1  # O(n)
out = list()  # O(n)
while a > 0:  # O(log(n)) по основанию 1,7
    out.append(arr[a])  # O(1)
    a = a // 1.7
out.merge_sort()  # O(n log(n))

# ассимптотическая сложность O(n log(n))