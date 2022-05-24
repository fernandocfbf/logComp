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
                CodeGenerator.write("mov EBX, EAX")
                return ("int", int(node1[1]+node2[1]))
            elif self.variant == "-":
                CodeGenerator.write("sub EAX, EBX")
                CodeGenerator.write("mov EBX, EAX")
                return ("int", int(node1[1]-node2[1]))
            elif self.variant == "*":
                CodeGenerator.write("imul EBX")
                CodeGenerator.write("mov EBX, EAX")
                return ("int", int(node1[1]*node2[1]))
            elif self.variant == "/":
                CodeGenerator.write("idiv EBX")
                CodeGenerator.write("mov EBX, EAX")
                return ("int", int(node1[1]/node2[1]))
            elif self.variant == "==":
                CodeGenerator.write("cmp EAX, EBX")
                CodeGenerator.write("call binop_je")
                return ("int", int(int(node1[1]) == int(node2[1])))
            elif self.variant == "<":
                CodeGenerator.write("cmp EAX, EBX")
                CodeGenerator.write("call binop_jl")
                return ("int", int(int(node1[1]) < int(node2[1])))
            elif self.variant == ">":
                CodeGenerator.write("cmp EAX, EBX")
                CodeGenerator.write("call binop_jg")
                return ("int", int(int(node1[1]) > int(node2[1])))
            else:
                raise Exception("Invalid token")

        raise Exception("Invalid expression")