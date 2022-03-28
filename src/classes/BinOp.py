from src.classes.Node import Node
class BinOp(Node):

    #@Override
    def Evaluate(self):
        node1 = self.children[0].Evaluate()
        node2 = self.children[1].Evaluate()
        if self.variant == "+":
            return node1+node2
        elif self.variant == "-":
            return node1-node2
        elif self.variant == "*":
            return node1*node2
        elif self.variant == "/":
            return node1/node2
        else:
            raise Exception("Invalid token")