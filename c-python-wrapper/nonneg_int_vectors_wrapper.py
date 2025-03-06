import ctypes


def c_array(list):
    return (ctypes.c_int * len(list))(*list)


def print_nonneg_int_vectors(n, maxValues):
    shared_lib = ctypes.CDLL('./nonneg_int_vectors.so')
    # shared_lib.generate_nonneg_int_vectors.argtypes = (ctypes.POINTER(ctypes.c_int),    # int* composition
    #                                                    ctypes.c_int,                    # int length
    #                                                    ctypes.c_int,                    # int index
    #                                                    ctypes.c_int,                    # int sum
    #                                                    ctypes.c_int,                    # int n
    #                                                    ctypes.POINTER(ctypes.c_int))    # int* maxValues

    composition = c_array([0] * len(maxValues))
    length = ctypes.c_int(len(maxValues))
    sum = ctypes.c_int(0)
    index = ctypes.c_int(0)
    n = ctypes.c_int(n)
    maxValues = c_array(maxValues)

    return shared_lib.generate_nonneg_int_vectors(composition, length, sum, index, n, maxValues)
