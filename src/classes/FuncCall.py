from src.classes.Node import Node
from src.classes.FuncTable import FuncTable
from src.classes.SymbolTable import SymbolTable

class FuncCall(Node):
    #@Override
    def Evaluate(self, st):
        #Corrigir
        type, ref = FuncTable.getFunction(self.variant).Evaluate(st)
        print('ref -> ', ref, type)
        symbol_table = SymbolTable()
        parameters = list()

        for i in range(1, len(ref.children)-1):
            parameters.append(self.children[i].variant)
            ref.children[i].Evaluate(symbol_table)
        
        for i in range(parameters):
            symbol_table.setSymbol(i, self.children[i].Evaluate())
        
        return ref.children[-1].Evaluate(symbol_table)