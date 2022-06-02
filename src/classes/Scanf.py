from src.classes.Node import Node
class Scanf(Node):

    #Override
    def Evaluate(self, st):
        _input = int(input())
        return ("int", _input)