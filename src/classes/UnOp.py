from src.classes.Node import Node
class UnOp(Node):

    #@Override
    def Evaluate(self, st):
        children = self.children[0].Evaluate()
        childrenType = children[0]
        childrenValue = children[1]
        if childrenType == "int":
            if self.variant == "-":
                return ('int', -childrenValue)
            elif self.variant == "+":
                return ('int', childrenValue)
            elif self.variant == "!":
                return ('int', not(childrenValue))
        else:
            raise Exception("Invalid expression")