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