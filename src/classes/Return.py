from src.classes.Node import Node
class Return(Node):

    #Override
    def Evaluate(self, st):
        #corrigir
        return self.children[0].Evaluate(st)