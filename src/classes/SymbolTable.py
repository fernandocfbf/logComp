class SymbolTable():
    symbols = dict()

    def setSymbol(symbol_name, symbol_value):
        SymbolTable.symbols[symbol_name] = symbol_value
        return

    def getSymbol(symbol_name):
        return SymbolTable.symbols[symbol_name]

