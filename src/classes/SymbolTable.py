from src.constants.types import TYPES

class SymbolTable():
    symbols = dict()

    def create(symbol):
        SymbolTable.symbols[symbol[1]] = (symbol[0], None)

    def setSymbol(symbol_name, symbol_value):
        if symbol_value[0] in TYPES:
            if (SymbolTable.symbols[symbol_name][0] == symbol_value[0]):
                SymbolTable.symbols[symbol_name] = (symbol_value[0], symbol_value[1])
                return
            raise Exception("Invalid assingment")
        raise Exception("Invalid type")

    def getSymbol(symbol_name):
        return SymbolTable.symbols[symbol_name]

