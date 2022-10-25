import cython

from libc.math cimport sqrt

def compute(end: cython.int, begin: cython.int = 1):
    pos: cython.int = begin
    fator: cython.int = 1000 * 1000

    with cython.nogil:
        while pos < end:
            pos += 1
            sqrt((pos - fator) * (pos - fator))