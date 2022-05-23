class CodeGenerator:
    assembly = str()

    def write(self, code):
        CodeGenerator.assembly += code 
        CodeGenerator.assembly += '\n'

    