from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("nonneg_int_matrices.pyx", language_level=3),
)
