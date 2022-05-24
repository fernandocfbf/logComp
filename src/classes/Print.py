from src.classes.Node import Node
from src.classes.CodeGenerator import CodeGenerator

class Print(Node):

    #Override
    def Evaluate(self):
        CodeGenerator.write("push EBX")
        CodeGenerator.write("call print")
        CodeGenerator.write("pop EBX")
        print(self.children[0].Evaluate()[1])
        return