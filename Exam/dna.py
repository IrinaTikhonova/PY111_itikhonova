from statistics import mode


def dna_reader(dna_checklist: list) -> str:
    """
        re-checking the dna list if dna reading results are not clear enough
        :param dna_checklist: list of string with same length
        :return: result of dna scanning -> string
        """
    if not dna_checklist:
        print("The result of first check is clear. No need to re-check")

    nucleotide = {i: [] for i, dna in enumerate(dna_checklist)}

    for index, dna in enumerate(dna_checklist):
        for j in range(0, len(dna)):
            nucleotide[j].append(dna[j])

    results_list = [v for k, v in nucleotide.items()]
    final_dna = list(map(mode, results_list))

    return "".join(final_dna)


# def get_key(d, value):
#     for k, v in d.items():
#         if v == value:
#             return k
#
# def dna_reader_2(list_of_results: list) -> str:
#     nucleotide = {"A": 0, "C": 0, "T": 0, "G": 0}
#     final_result = []
#     for i, dna in enumerate(list_of_results):
#         for j in range(0, len(dna)):
#             nucleotide[dna[j]] += 1
#
#         max_count = max(nucleotide.values())
#         final_result.append(get_key(nucleotide, max_count))
#
#     return str.join("", final_result)


if __name__ == '__main__':
    list1 = ["ATTA", "ACTA", "AGCA", "ACAA"]
    list2 = []
    print(dna_reader(list1))
    print(dna_reader(list2))
    # print(dna_reader_2(list1))
