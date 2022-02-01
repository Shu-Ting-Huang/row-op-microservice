from __init__ import RowOpSequence, next_row_op_Gauss_Jordan

from sympy import Matrix, Rational, Symbol, eye
from random import choice

for _ in range(5):
    m = choice(range(1,15))
    n = choice(range(1,15))
    A = Matrix(m, n, lambda i,j: Rational(choice(range(-100,100)),choice(range(1,10))))
    row_op_seq = RowOpSequence(A)
    while next_row_op_Gauss_Jordan(row_op_seq.matrices[-1]) != None:
        row_op_seq.add_step(next_row_op_Gauss_Jordan(row_op_seq.matrices[-1]))
    assert row_op_seq.matrices[-1] == A.rref()[0]

A = Matrix([[Matrix([['a', 'b'], ['c', 'd']]),eye(2)]])
row_op_seq = RowOpSequence(A)
while next_row_op_Gauss_Jordan(row_op_seq.matrices[-1]) != None:
    row_op_seq.add_step(next_row_op_Gauss_Jordan(row_op_seq.matrices[-1]))
assert row_op_seq.matrices[-1][:,0:2] == eye(2)
assert row_op_seq.matrices[-1][:,2:4]*(Symbol('a')*Symbol('d')-Symbol('b')*Symbol('c')) == Matrix([['d', '-b'], ['-c', 'a']])
assert len(row_op_seq.row_ops) == 4
assert len(row_op_seq.matrices) == 5


print("\nAll tests are passed")