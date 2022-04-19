import sys

from src.classes.Parser import Parser

file = sys.argv[1]
with open(file) as f:
    exp = f.read()
    exp_result = Parser.run(exp) # calculates exp
    
if exp_result != None:
    exp_result.Evaluate()
