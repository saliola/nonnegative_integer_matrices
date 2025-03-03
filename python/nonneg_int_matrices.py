def nonneg_int_vectors_iter(n, ceiling):
    r"""
    Vectors of nonnegative integers that sum to `n`
    whose parts are bounded according to `ceiling`.

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
            yield [n]
    else:
        for first_entry in range(min(ceiling[0], n) + 1):
            for vec in nonneg_int_vectors_iter(n - first_entry, ceiling[1:]):
                yield [first_entry] + vec


def nonneg_int_matrices_iter(row_sums, col_sums):
    r"""
    Matrices of nonnegative integers with prescribed row and column sums.

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
        yield [col_sums]
    else:
        for first_row in nonneg_int_vectors_iter(row_sums[0], ceiling=col_sums):
            for mat in nonneg_int_matrices_iter(row_sums[1:], [ci - fi for (ci, fi) in zip(col_sums, first_row)]):
                yield [first_row] + mat


if __name__ == "__main__":
    row_sums = [3, 1, 5]
    col_sums = [5, 4]
    for mat in nonneg_int_matrices_iter(row_sums, col_sums):
        print(mat)
