from src.classes.Node import Node
from src.classes.CodeGenerator import CodeGenerator

class IntVal(Node):

    #@Override
    def Evaluate(self):
        CodeGenerator.write("MOV EBX, {0}".format(self.variant))
        return ("int", self.variant)