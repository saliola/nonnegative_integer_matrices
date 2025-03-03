import numpy as np
cimport numpy as np

def nonneg_int_vectors_iter(int n, np.ndarray ceiling):
    cdef int first_entry

    if len(ceiling) == 1:
        if n <= ceiling[0]:
            yield np.array([n], dtype=np.int32)
    else:
        for first_entry in range(min(ceiling[0], n) + 1):
            for sub_vec in nonneg_int_vectors_iter(n - first_entry, ceiling[1:]):
                prefix = np.array([first_entry], dtype=np.int32)
                yield np.concatenate([prefix, sub_vec])


def nonneg_int_matrices_iter(np.ndarray row_sums, np.ndarray col_sums):
    if len(row_sums) == 1:
        yield np.array([col_sums], dtype=np.int32)
    else:
        for first_row in nonneg_int_vectors_iter(row_sums[0], ceiling=col_sums):
            for mat in nonneg_int_matrices_iter(row_sums[1:], col_sums - first_row):
                yield np.concatenate([[first_row], mat])

