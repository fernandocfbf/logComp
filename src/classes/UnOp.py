from src.classes.Node import Node
class UnOp(Node):

    #@Override
    def Evaluate(self):
        if self.variant == "-":
            return - self.children[0].Evaluate()
        elif self.variant == "+":
            return self.children[0].Evaluate()
        elif self.variant == "!":
            return not(self.children[0].Evaluate())