from src.classes.Node import Node
class UnOp(Node):

    #@Override
    def Evaluate(self):
        node1 = self.children[0].Evaluate()
        return node1