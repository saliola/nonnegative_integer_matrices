if __name__ == "__main__":
    import numpy as np
    from nonneg_int_matrices import nonneg_int_matrices_iter
    row_sums = np.array([3, 1, 5], dtype=np.int32)
    col_sums = np.array([5, 4], dtype=np.int32)
    for mat in nonneg_int_matrices_iter(row_sums, col_sums):
        print(mat)
