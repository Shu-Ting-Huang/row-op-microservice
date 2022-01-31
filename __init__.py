from sympy import simplify

# An object of RowOpSequence consists of a sequence of matrices connected by elementary row operations 
class RowOpSequence:
    # Initialize an object with a single matrix
    def __init__(self, A):
        self.matrices = [A]
        self.row_ops = []
        
    # Undo the last step of row operation
    def undo(self):
        self.row_ops.pop()
        self.matrices.pop()
        
    # Add one more step to the sequence of row operations
    # row_op can be
    # (1) {"op": "n->n+km", "k": k, "row": n, "row2": m}
    # (2) {"op": "n<->m", "row1": n, "row2": m}
    # (3) {"op": "n->kn", "k": k, "row": n}
    def add_step(self, row_op):
        self.matrices.append(simplify(self.matrices[-1].elementary_row_op(**row_op)))
        self.row_ops.append(row_op)

def next_row_op(A):
    # A is empty matrix
    if len(A) == 0:
        return None

    # The first column of A is zero vector
    elif A[:,0].is_zero_matrix:
        return next_row_op(A[:,1:])

    # A[0,0] is zero
    elif A[0,0] == 0:
        return {"op": "n<->m", "row1": 0, "row2": min(i for i in range(1, A.shape[0]) if A[i,0] != 0)}
    
    # A[0,0] is the only non-zero entry in the first column
    elif A[1:,0].is_zero_matrix:
        temp_row_op = next_row_op(A[1:,1:])
        for key in temp_row_op.keys():
            if key.startswith("row"):
                temp_row_op[key] += 1
        return temp_row_op
    
    # A[1:,0] has some non-zero entries
    else:
        i = min(i for i in range(1, A.shape[0]) if A[i,0] != 0)
        return {"op": "n->n+km", "k": -A[i,0]/A[0,0], "row": i, "row2": 0}