from src.classes.Node import Node
class UnOp(Node):

    #@Override
    def Evaluate(self):
        if self.variant == "-":
            return - self.children[0].Evaluate()
        return self.children[0].Evaluate()