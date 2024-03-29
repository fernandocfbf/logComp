from src.classes.Node import Node
from src.classes.CodeGenerator import CodeGenerator
class UnOp(Node):

    #@Override
    def Evaluate(self):
        children = self.children[0].Evaluate()
        CodeGenerator.write("PUSH EBX")
        childrenType = children[0]
        childrenValue = children[1]
        if childrenType == "int":
            if self.variant == "-":
                CodeGenerator.write("NEG EBX")
                return ('int', -childrenValue)
            elif self.variant == "+":
                #CodeGenerator.write("any-unOp EBX") #Corrigir
                return ('int', childrenValue)
            elif self.variant == "!":
                CodeGenerator.write("NOT EBX")
                return ('int', not(childrenValue))
        else:
            raise Exception("Invalid expression")