from src.classes.Node import Node
class UnOp(Node):

    #@Override
    def Evaluate(self):
        children = self.children[0].Evaluate()[0]
        childrenType = children[0]
        childrenValue = children[1]
        if childrenType == "int":
            if self.variant == "-":
                return tuple('', -childrenValue)
            elif self.variant == "+":
                return tuple('', childrenValue)
            elif self.variant == "!":
                return tuple('', not(childrenValue))
        else:
            raise Exception("Invalid expression")