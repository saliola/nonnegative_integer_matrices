if __name__ == "__main__":
    from nonneg_int_matrices import nonneg_int_matrices_iter
    row_sums = [3, 1, 5]
    col_sums = [5, 4]
    for mat in nonneg_int_matrices_iter(row_sums, col_sums):
        print(mat)
