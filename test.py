from __init__ import RowOpSequence, next_row_op_Gauss_Jordan

from sympy import Matrix, Rational
from random import choice

for _ in range(5):
    m = choice(range(1,15))
    n = choice(range(1,15))
    A = Matrix(m, n, lambda i,j: Rational(choice(range(-100,100)),choice(range(1,10))))
    row_op_seq = RowOpSequence(A)
    while next_row_op_Gauss_Jordan(row_op_seq.matrices[-1]) != None:
        row_op_seq.add_step(next_row_op_Gauss_Jordan(row_op_seq.matrices[-1]))
    assert row_op_seq.matrices[-1] == A.rref()[0]

print("\nAll tests are passed")