class Node():
    i = 0

    def __init__(self, variant, children):
        self.variant = variant #node value (string)
        self.children = children; #child nodes (list)
        self.i = self.NewId()

    def NewId(self):
        Node.i += 1
        return Node.i

    def Evaluate():
        return 