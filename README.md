# Generating nonnegative integer matrices with prescribed row and column sums

Implementations in different languages of an algorithm to generate nonnegative
integer matrices with prescribed row and column sums. These are also known as
[contingency tables](https://en.wikipedia.org/wiki/Contingency_table).


## python

The file `nonneg_int_matrices.py` contains an example/test.
```bash
$ cd python
$ python nonneg_int_matrices.py
[[0, 3], [0, 1], [5, 0]]
[[0, 3], [1, 0], [4, 1]]
[[1, 2], [0, 1], [4, 1]]
[[1, 2], [1, 0], [3, 2]]
[[2, 1], [0, 1], [3, 2]]
[[2, 1], [1, 0], [2, 3]]
[[3, 0], [0, 1], [2, 3]]
[[3, 0], [1, 0], [1, 4]]
```

## numpy

Install numpy if it is not already installed:
```bash
$ pip install numpy
```

The file `nonneg_int_matrices.py` contains an example/test.
```bash
$ cd numpy
$ python nonneg_int_matrices.py
[[0 3]
 [0 1]
 [5 0]]
[[0 3]
 [1 0]
 [4 1]]
[[1 2]
 [0 1]
 [4 1]]
[[1 2]
 [1 0]
 [3 2]]
[[2 1]
 [0 1]
 [3 2]]
[[2 1]
 [1 0]
 [2 3]]
[[3 0]
 [0 1]
 [2 3]]
[[3 0]
 [1 0]
 [1 4]]
```

## cython

Install cython if it is not already installed:
```bash
$ pip install cython
```

The file `nonneg_int_matrices.py` contains an example/test.
```bash
$ cd cython
$ make
$ python nonneg_int_matrices.py
[[0, 3], [0, 1], [5, 0]]
[[0, 3], [1, 0], [4, 1]]
[[1, 2], [0, 1], [4, 1]]
[[1, 2], [1, 0], [3, 2]]
[[2, 1], [0, 1], [3, 2]]
[[2, 1], [1, 0], [2, 3]]
[[3, 0], [0, 1], [2, 3]]
[[3, 0], [1, 0], [1, 4]]
```

## cython with numpy

Install cython and numpy if not already installed:
```bash
$ pip install cython
$ pip install numpy
```

The file `nonneg_int_matrices.py` contains an example/test.
```bash
$ cd cython-with-numpy
$ make
$ python nonneg_int_matrices.py
[[0 3]
 [0 1]
 [5 0]]
[[0 3]
 [1 0]
 [4 1]]
[[1 2]
 [0 1]
 [4 1]]
[[1 2]
 [1 0]
 [3 2]]
[[2 1]
 [0 1]
 [3 2]]
[[2 1]
 [1 0]
 [2 3]]
[[3 0]
 [0 1]
 [2 3]]
[[3 0]
 [1 0]
 [1 4]]
```
