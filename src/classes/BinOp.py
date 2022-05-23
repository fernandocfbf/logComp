from src.classes.Node import Node
from src.classes.CodeGenerator import CodeGenerator
class BinOp(Node):

    #@Override
    def Evaluate(self):
        node1 = self.children[0].Evaluate()
        CodeGenerator.write("push EBX")
        node2 = self.children[1].Evaluate()
        CodeGenerator.write("pop EAX")

        if node1[0] == node2[0] == "int":
            if self.variant == "+":
                CodeGenerator.write("add EAX, EBX")
                #return ("int", int(node1[1]+node2[1]))
            elif self.variant == "-":
                CodeGenerator.write("sub EAX, EBX")
                #return ("int", int(node1[1]-node2[1]))
            elif self.variant == "*":
                CodeGenerator.write("imul EAX, EBX")
                #return ("int", int(node1[1]*node2[1]))
            elif self.variant == "/":
                CodeGenerator.write("idiv EAX, EBX")
                #return ("int", int(node1[1]/node2[1]))
            elif self.variant == "==":
                CodeGenerator.write("je EAX, EBX")
                #return ("int", int(int(node1[1]) == int(node2[1])))
            elif self.variant == "<":
                CodeGenerator.write("jl EAX, EBX")
                #return ("int", int(int(node1[1]) < int(node2[1])))
            elif self.variant == ">":
                CodeGenerator.write("jg EAX, EBX")
                #return ("int", int(int(node1[1]) > int(node2[1])))
            elif self.variant == "||":
                CodeGenerator.write("OR EAX, EBX")
                #return ("int", node1[1] or node2[1])
            elif self.variant == "&&":
                CodeGenerator.write("AND EAX, EBX")
                #return ("int", node1[1] and node2[1])
            elif self.variant == ".":
                CodeGenerator.write("any-binOp EAX, EBX") #Corrigir
                #return ("str", str(node1[1]) + str(node2[1]))
            else:
                raise Exception("Invalid token")
        elif node1[0] == node2[0] == "str":
            if self.variant == "==":
                CodeGenerator.write("je EAX, EBX")
                #return ("int", int(node1[1] == node2[1]))
            elif self.variant == "<":
                CodeGenerator.write("jl EAX, EBX")
                #return ("int", int(node1[1] < node2[1]))
            elif self.variant == ">":
                CodeGenerator.write("jg EAX, EBX")
                #return ("int", int(node1[1] > node2[1]))
            elif self.variant == ".":
                CodeGenerator.write("any-binOp EAX, EBX") #Corrigir
                #return ("str", str(node1[1]) + str(node2[1]))
            return ("str", str(node1[1]) + str(node2[1]))
        elif node1[0] != node2[1]:
            if self.variant == ".":
                CodeGenerator.write("any-binOp EAX, EBX") #Corrigir
                #return ("str", str(node1[1]) + str(node2[1]))

        raise Exception("Invalid expression")