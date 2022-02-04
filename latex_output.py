from sympy import Rational
from sympy import latex

def number2latex(x, omit_one=False):
    if omit_one:
        if x == 1:
            return ''
        elif x == -1:
            return '-'
        else:
            return number2latex(x)
    else:
        if isinstance(x,(int,Rational)):
            return latex(x)

def matrix2latex(A):
    row_strings = []
    for row in A.tolist():
        row_strings.append(' & '.join(number2latex(entry) for entry in row))
    return '\\begin{pmatrix}\n' + '\\\\[4pt]\n'.join(row_strings) + '\n\\end{pmatrix}'

def row_op2latex(row_op):
    if row_op['op'] == 'n->n+km':
        k = row_op['k']
        m = row_op['row2'] + 1
        n = row_op['row'] + 1
        return number2latex(k, omit_one=True) + 'R_{' + str(m) + '}+R_{' + str(n) + '}\\rightarrow R_{' + str(n) +'}'
    elif row_op['op'] == 'n<->m':
        m = row_op['row1'] + 1
        n = row_op['row2'] + 1
        return 'R_{' + str(m) + '}\\leftrightarrow R_{' + str(n) + '}'
    else:
        k = row_op['k']
        n = row_op['row'] + 1
        return number2latex(k, omit_one=True) + 'R_{' + str(n) + '}\\rightarrow R_{' + str(n) + '}'

def row_op_seq2latex(row_op_seq):
    pass