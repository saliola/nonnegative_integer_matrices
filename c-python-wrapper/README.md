# Accessing a C function from within Python

We have a C file `nonneg_int_vectors.c` that contains a function called
`generate_nonneg_int_vectors`. The following expains how one can access this
function from Python.

## Compile the C code to a shared library file

```bash
gcc -fPIC -shared -o nonneg_int_vectors.so nonneg_int_vectors.c
```

## Call the function `generate_nonneg_int_vectors` from Python

```python
>>> import ctypes
>>> def c_array(list):
>>>     return (ctypes.c_int * len(list))(*list)
>>> shared_lib = ctypes.CDLL('./nonneg_int_vectors.so')
>>> composition = c_array([0, 0, 0, 0])
>>> length = ctypes.c_int(4)
>>> sum = ctypes.c_int(0)
>>> index = ctypes.c_int(0)
>>> n = ctypes.c_int(9)
>>> maxValues = c_array([3, 5, 1, 2])
>>> shared_lib.generate_nonneg_int_vectors(composition, length, sum, index, n, maxValues)
[1, 5, 1, 2]
[2, 4, 1, 2]
[2, 5, 0, 2]
[2, 5, 1, 1]
[3, 3, 1, 2]
[3, 4, 0, 2]
[3, 4, 1, 1]
[3, 5, 0, 1]
[3, 5, 1, 0]
34390016
```

## Write a wrapper

The above can be wrapped in a Python function.
```python
# filename: nonneg_int_vectors_wrapper.py
import ctypes

def c_array(list):
    return (ctypes.c_int * len(list))(*list)

def print_nonneg_int_vectors(n, maxValues):
    shared_lib = ctypes.CDLL('./nonneg_int_vectors.so')
    composition = c_array([0] * len(maxValues))
    length = ctypes.c_int(len(maxValues))
    sum = ctypes.c_int(0)
    index = ctypes.c_int(0)
    n = ctypes.c_int(n)
    maxValues = c_array(maxValues)
    shared_lib.generate_nonneg_int_vectors(composition, length, sum, index, n, maxValues)
```
Then one can import and use the function as usual:
```python
>>> from nonneg_int_vectors_wrapper import print_nonneg_int_vectors
>>> print_nonneg_int_vectors(9, [3, 5, 1, 2])
[1, 5, 1, 2]
[2, 4, 1, 2]
[2, 5, 0, 2]
[2, 5, 1, 1]
[3, 3, 1, 2]
[3, 4, 0, 2]
[3, 4, 1, 1]
[3, 5, 0, 1]
[3, 5, 1, 0]
```
