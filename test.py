from __init__ import RowOpSequence, next_row_op_Gauss_Jordan

from sympy import Matrix, Rational, Symbol, eye, GF, prime
from random import choice

def random_rational():
    return Rational(choice(range(-100,100)), choice(range(1,50)))

for _ in range(5):
    m = choice(range(1,8))
    n = choice(range(1,8))
    A = Matrix(m, n, lambda i,j: random_rational())
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

for _ in range(5):
    m = choice(range(1,8))
    n = choice(range(1,8))
    p = prime(choice(range(1,100)))
    K = GF(p)
    A = Matrix(m, n, lambda i,j: K(choice(range(p))))
    row_op_seq = RowOpSequence(A)
    while next_row_op_Gauss_Jordan(row_op_seq.matrices[-1]) != None:
        row_op_seq.add_step(next_row_op_Gauss_Jordan(row_op_seq.matrices[-1]))
    assert row_op_seq.matrices[-1] == A.rref()[0]

print("\nAll tests are passed")