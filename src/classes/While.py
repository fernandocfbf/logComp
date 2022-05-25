from src.classes.Node import Node
from src.classes.CodeGenerator import CodeGenerator

class While(Node):
    
    #Override
    def Evaluate(self):
        CodeGenerator.write("LOOP_{0}".format(self.i))
        self.children[0].Evaluate()
        CodeGenerator.write("CMP EBX, False")
        CodeGenerator.write("JE EXIT_{0}".format(self.i))
        self.children[1].Evaluate()
        CodeGenerator.write("JMP LOOP_{0}".format(self.i))
        CodeGenerator.write("EXIT_{0}".format(self.i))
