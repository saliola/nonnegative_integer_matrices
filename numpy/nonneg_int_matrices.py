import numpy as np


def nonneg_int_vectors_iter(n, ceiling):
    r"""
    Vectors of nonnegative integers that sum to `n`
    whose parts are bounded according to `ceiling`.

    >>> from nonneg_int_matrices import nonneg_int_vectors_iter
    >>> for v in nonneg_int_vectors_iter(5, [3, 1, 5]):
    ...     print(v)
    [0, 0, 5]
    [0, 1, 4]
    [1, 0, 4]
    [1, 1, 3]
    [2, 0, 3]
    [2, 1, 2]
    [3, 0, 2]
    [3, 1, 1]
    """
    if len(ceiling) == 1:
        if n <= ceiling[0]:
            yield np.array([n], dtype=np.int32)
    else:
        for first_entry in range(min(ceiling[0], n) + 1):
            for sub_vec in nonneg_int_vectors_iter(n - first_entry, ceiling[1:]):
                prefix = np.array([first_entry], dtype=np.int32)
                yield np.concatenate([prefix, sub_vec])


def nonneg_int_matrices_iter(row_sums, col_sums):
    r"""
    Matrices of nonnegative integers with prescribed row and column sums.

    >>> from nonneg_int_matrices import nonneg_int_matrices_iter
    >>> for m in nonneg_int_matrices_iter([3,2,2], [2,5]):
    ...     print(m)
    [[0, 3], [0, 2], [2, 0]]
    [[0, 3], [1, 1], [1, 1]]
    [[0, 3], [2, 0], [0, 2]]
    [[1, 2], [0, 2], [1, 1]]
    [[1, 2], [1, 1], [0, 2]]
    [[2, 1], [0, 2], [0, 2]]
    """
    if sum(row_sums) != sum(col_sums):
        return

    if len(row_sums) == 1:
        yield np.array([col_sums], dtype=np.int32)
    else:
        for first_row in nonneg_int_vectors_iter(row_sums[0], ceiling=col_sums):
            for mat in nonneg_int_matrices_iter(row_sums[1:], col_sums - first_row):
                yield np.concatenate([[first_row], mat])


if __name__ == "__main__":
    row_sums = np.array([3, 1, 5], dtype=np.int32)
    col_sums = np.array([5, 4], dtype=np.int32)
    for mat in nonneg_int_matrices_iter(row_sums, col_sums):
        print(mat)
