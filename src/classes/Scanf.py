from src.classes.Node import Node
class Scanf(Node):

    #Override
    def Evaluate(self):
        return int(input())