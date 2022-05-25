from src.classes.Node import Node
from src.classes.CodeGenerator import CodeGenerator
class BinOp(Node):

    #@Override
    def Evaluate(self):
        node1 = self.children[0].Evaluate()
        CodeGenerator.write("PUSH EBX")
        
        node2 = self.children[1].Evaluate()
        CodeGenerator.write("POP EAX")

        if node1[0] == node2[0] == "int":
            if self.variant == "+":
                CodeGenerator.write("ADD EAX, EBX")
                CodeGenerator.write("MOV EBX, EAX")
                return ("int", int(node1[1]+node2[1]))
            elif self.variant == "-":
                CodeGenerator.write("SUB EAX, EBX")
                CodeGenerator.write("MOV EBX, EAX")
                return ("int", int(node1[1]-node2[1]))
            elif self.variant == "*":
                CodeGenerator.write("IMUL EBX")
                CodeGenerator.write("MOV EBX, EAX")
                return ("int", int(node1[1]*node2[1]))
            elif self.variant == "/":
                CodeGenerator.write("IDIV EBX")
                CodeGenerator.write("MOV EBX, EAX")
                return ("int", int(node1[1]/node2[1]))
            elif self.variant == "==":
                CodeGenerator.write("CMP EAX, EBX")
                CodeGenerator.write("CALL binop_je")
                return ("int", int(int(node1[1]) == int(node2[1])))
            elif self.variant == "<":
                CodeGenerator.write("CMP EAX, EBX")
                CodeGenerator.write("CALL binop_jl")
                return ("int", int(int(node1[1]) < int(node2[1])))
            elif self.variant == ">":
                CodeGenerator.write("CMP EAX, EBX")
                CodeGenerator.write("CALL binop_jg")
                return ("int", int(int(node1[1]) > int(node2[1])))
            else:
                raise Exception("Invalid token")

        raise Exception("Invalid expression")