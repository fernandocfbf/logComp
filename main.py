import sys
from src.classes.Parser import Parser
from src.classes.CodeGenerator import CodeGenerator

file = sys.argv[1]
with open(file) as f:
    exp = f.read()
    exp_result = Parser.run(exp) # calculates exp
    
if exp_result != None:
    exp_result.Evaluate()
    print(sys.argv[1])
    CodeGenerator.dump(sys.argv[1].replace(".c", ".asm"))
