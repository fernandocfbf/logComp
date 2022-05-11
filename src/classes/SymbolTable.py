from src.constants.types import TYPES

class SymbolTable():
    symbols = dict()

    def setSymbol(symbol_name, symbol_type, symbol_value):
        if symbol_type in TYPES:
            SymbolTable.symbols[symbol_name] = tuple(symbol_type, symbol_value)
            return
        raise Exception("Invalid type")

    def getSymbol(symbol_name):
        return SymbolTable.symbols[symbol_name]

