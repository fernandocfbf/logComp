from src.classes.Node import Node
from src.classes.CodeGenerator import CodeGenerator

class If(Node):
    
    #Override
    def Evaluate(self):
        CodeGenerator.write("if_{0}:".format(self.i))
        self.children[0].Evaluate()
        CodeGenerator.write("CMP EBX, False")
        CodeGenerator.write("JE else_{0}".format(self.i))
        self.children[1].Evaluate()
        CodeGenerator.write("JMP end_if_{0}".format(self.i))
        CodeGenerator.write("else_{0}:".format(self.i))

        if len(self.children) > 2:
            self.children[2].Evaluate()
        CodeGenerator.write("end_if_{0}:".format(self.i))
        