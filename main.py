import sys

from src.classes.Parser import Parser
from src.classes.FuncCall import FuncCall
from src.classes.SymbolTable import SymbolTable

file = sys.argv[1]
with open(file) as f:
    exp = f.read()
    exp_result = Parser.run(exp) 
    
if exp_result != None:
    st_main = SymbolTable()
    main = FuncCall('main', list())
    exp_result.children.append(main)
    exp_result.Evaluate(st_main)
