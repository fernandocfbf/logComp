from src.classes.Node import Node
class Scanf(Node):

    #Override
    def Evaluate(self):
        _input = int(input())
        return ("int", _input)