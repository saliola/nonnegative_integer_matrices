from typing import List, Iterator


def nonneg_int_vectors_iter(int n, List[int] ceiling) -> Iterator[List[int]]:
    cdef int first_entry

    if len(ceiling) == 1:
        if n <= ceiling[0]:
            yield [n]
    else:
        for first_entry in range(min(ceiling[0], n) + 1):
            for sub_vec in nonneg_int_vectors_iter(n - first_entry, ceiling[1:]):
                yield [first_entry] + sub_vec


def nonneg_int_matrices_iter(List[int] row_sums, List[int] col_sums) -> Iterator[List[List[int]]]:
    if len(row_sums) == 1:
        yield [col_sums]
    else:
        for first_row in nonneg_int_vectors_iter(row_sums[0], ceiling=col_sums):
            truncated_row_sums = row_sums[1:]
            truncated_col_sums = [col_sums[i] - first_row[i] for i in range(len(col_sums))]
            for mat in nonneg_int_matrices_iter(truncated_row_sums, truncated_col_sums):
                yield [first_row] + mat
