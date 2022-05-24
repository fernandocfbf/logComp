from src.constants.types import TYPES
from src.classes.CodeGenerator import CodeGenerator

class SymbolTable():
    symbols = dict()
    shift = 4

    def create(symbol):
        if symbol[1] not in SymbolTable.symbols:
            CodeGenerator.write("push DWORD 0")
            SymbolTable.symbols[symbol[1]] = (symbol[0], None, SymbolTable.shift)
            SymbolTable.shift += 4
        else:
            raise Exception("Cannot subscribe variable")

    def setSymbol(symbol_name, symbol_value):
        if symbol_value[0] in TYPES:
            if (SymbolTable.symbols[symbol_name][0] == symbol_value[0]):
                CodeGenerator.write("mov [EBP-{0}], EBX".format(SymbolTable.symbols[symbol_name][2]))
                SymbolTable.symbols[symbol_name] = (
                    SymbolTable.symbols[symbol_name][0],
                    symbol_value[1],
                    SymbolTable.symbols[symbol_name][2])
                return
            raise Exception("Invalid assingment")
        raise Exception("Invalid type")

    def getSymbol(symbol_name):
        CodeGenerator.write("mov EBX, [EBP - {0}]".format(SymbolTable.symbols[symbol_name][2]))
        return SymbolTable.symbols[symbol_name]

