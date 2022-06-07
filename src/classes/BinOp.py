from src.classes.Node import Node
class BinOp(Node):

    #@Override
    def Evaluate(self, st):
        node1 = self.children[0].Evaluate(st)
        node2 = self.children[1].Evaluate(st)

        if node1[0] == node2[0] == "int":
            if self.variant == "+":
                return ("int", int(node1[1]+node2[1]))
            elif self.variant == "-":
                return ("int", int(node1[1]-node2[1]))
            elif self.variant == "*":
                return ("int", int(node1[1]*node2[1]))
            elif self.variant == "/":
                return ("int", int(node1[1]/node2[1]))
            elif self.variant == "==":
                return ("int", int(int(node1[1]) == int(node2[1])))
            elif self.variant == "<":
                return ("int", int(int(node1[1]) < int(node2[1])))
            elif self.variant == ">":
                return ("int", int(int(node1[1]) > int(node2[1])))
            elif self.variant == "||":
                return ("int", node1[1] or node2[1])
            elif self.variant == "&&":
                return ("int", node1[1] and node2[1])
            elif self.variant == ".":
                return ("str", str(node1[1]) + str(node2[1]))
            else:
                raise Exception("Invalid token")
        elif node1[0] == node2[0] == "str":
            if self.variant == "==":
                return ("int", int(node1[1] == node2[1]))
            elif self.variant == "<":
                return ("int", int(node1[1] < node2[1]))
            elif self.variant == ">":
                return ("int", int(node1[1] > node2[1]))
            elif self.variant == ".":
                return ("str", str(node1[1]) + str(node2[1]))
            return ("str", str(node1[1]) + str(node2[1]))
        elif node1[0] != node2[1]:
            if self.variant == ".":
                return ("str", str(node1[1]) + str(node2[1]))

        raise Exception("Invalid expression")