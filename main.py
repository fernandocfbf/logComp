import sys

from src.classes.Parser import Parser

expression = sys.argv[1]
exp_result = Parser.run(expression) # calculates exp
if exp_result != None:
    print(int(exp_result))