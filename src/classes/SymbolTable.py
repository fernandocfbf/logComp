class SymbolTable():
    symbols = dict()

    def setSymbol(self, symbol_name, symbol_value):
        self.symbols[symbol_name] = symbol_value
        return

    def getSymbol(self, symbol_name):
        return self.symbols[symbol_name]

