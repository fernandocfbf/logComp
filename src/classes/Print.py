from src.classes.Node import Node
from src.classes.CodeGenerator import CodeGenerator

class Print(Node):

    #Override
    def Evaluate(self):
        self.children[0].Evaluate()
        CodeGenerator.write("PUSH EBX")
        CodeGenerator.write("CALL print")
        CodeGenerator.write("POP EBX")
        return