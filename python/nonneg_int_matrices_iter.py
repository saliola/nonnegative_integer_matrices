def nonneg_int_vectors_iter(n, length, ceiling):
    r"""
    Vectors of nonnegative integers
    of prescribed `length` and sum `n`
    whose parts are bounded according to `ceiling`.

    >>> iter = nonneg_int_vectors_iter(5, 3, [3, 1, 5])
    >>> for v in iter:
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
    assert length == len(ceiling)

    if length == 1:
        if n <= ceiling[0]:
            yield [n]
    else:
        for first_entry in range(min(ceiling[0], n) + 1):
            for vec in nonneg_int_vectors_iter(n - first_entry, length - 1, ceiling[1:]):
                yield [first_entry] + vec


def nonneg_int_matrices_iter(row_sums, col_sums):
    r"""
    Matrices of nonnegative integers
    with prescribed row and column sums.

    >>> iter = nonneg_int_matrices_iter([3,2,2], [2,5])
    >>> for m in iter:
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
        for first_row in nonneg_int_vectors_iter(row_sums[0],
                                                 length=len(col_sums),
                                                 ceiling=col_sums):
            truncated_row_sums = row_sums[1:]
            truncated_col_sums = [col_sums[i] - first_row[i] for i in range(len(col_sums))]
            for mat in nonneg_int_matrices_iter(truncated_row_sums, truncated_col_sums):
                yield [first_row] + mat
