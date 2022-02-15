import os
import sys
from string import Template
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread

# Add the parent directory to the path and import row_op_seq2latex
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
from latex_output import row_op_seq2latex

# change to the directory in which THIS SCRIPT is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Define the main test function
def test_latex_output(row_op_seq):
    # Fill in the template
    with open("latex_template.html", "r") as f:
        template = Template(f.read())
    html_content = template.substitute(latex_string=row_op_seq2latex(row_op_seq).replace('\n', '\n' + ' '*8))

    # Host it locally
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(html_content, "utf-8"))
    server = HTTPServer(("localhost", 8000), Handler)
    server_thread = Thread(target=lambda:[server.handle_request(), server.handle_request()] and None)
    server_thread.start()

    # Open it in a browser
    os.system("start http://localhost:8000/")

from sympy import Matrix
from __init__ import *
A = Matrix([[-2,-1,-3,7], [1,-5,0,0], [3,5,3,2]])
A = Matrix([[1,-1,1,5], [3,-5,0,0], [0,5,-3,0]])
row_op_seq = RowOpSequence(A)
while next_row_op_Gauss_Jordan(row_op_seq.matrices[-1]) != None:
    row_op_seq.add_step(next_row_op_Gauss_Jordan(row_op_seq.matrices[-1]))
test_latex_output(row_op_seq)