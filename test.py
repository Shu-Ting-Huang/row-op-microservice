from __init__ import RowOpSequence, next_row_op_Gauss_Jordan

from sympy import Matrix, Rational

A = Matrix([[-2,-1,-3,7],[1,-5,0,0],[3,5,3,2]])
seq = RowOpSequence(A)
while next_row_op_Gauss_Jordan(seq.matrices[-1]) != None:
    seq.add_step(next_row_op_Gauss_Jordan(seq.matrices[-1]))
assert seq.matrices[-1] == Matrix([[1,0,0,5],[0,1,0,1],[0,0,1,-6]])

A = Matrix([[1,-1,1,5],[3,-5,0,0],[0,5,-3,0]])
seq = RowOpSequence(A)
while next_row_op_Gauss_Jordan(seq.matrices[-1]) != None:
    seq.add_step(next_row_op_Gauss_Jordan(seq.matrices[-1]))
assert seq.matrices[-1] == Matrix([[1,0,0,Rational(25,7)],[0,1,0,Rational(15,7)],[0,0,1,Rational(25,7)]])

A = Matrix([[564,51,1489,524,74],[0,1,-15,1900,-9999],[4564,-88,-776,3,901],[542,5,578,5236,41]])
seq = RowOpSequence(A)
while next_row_op_Gauss_Jordan(seq.matrices[-1]) != None:
    seq.add_step(next_row_op_Gauss_Jordan(seq.matrices[-1]))
assert seq.matrices[-1] == A.rref()[0]

print("\nAll tests are passed")