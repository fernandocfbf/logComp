from src.constants.types import TYPES

class SymbolTable():
    def __init__(self):
        self.symbols = dict()
        
    def create(self, symbol):
        if symbol[1] not in self.symbols:
            self.symbols[symbol[1]] = (symbol[0], None)
        else:
            raise Exception("Cannot subscribe variable")

    def setSymbol(self, symbol_name, symbol_value):
        if symbol_value[0] in TYPES:
            if (self.symbols[symbol_name][0] == symbol_value[0]):
                self.symbols[symbol_name] = (symbol_value[0], symbol_value[1])
                return
            raise Exception("Invalid assingment")
        raise Exception("Invalid type")

    def getSymbol(self, symbol_name):
        return self.symbols[symbol_name]

