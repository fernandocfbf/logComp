from src.classes.Node import Node
from src.classes.SymbolTable import SymbolTable

class VarDec(Node):
    #@Override
    def Evaluate(self, st):
        for children in self.children:
            st.create(children)
        return