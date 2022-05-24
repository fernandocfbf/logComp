from src.constants.asm import HEADER, FOOTER

class CodeGenerator:
    assembly = str()

    def write(code):
        CodeGenerator.assembly += code 
        CodeGenerator.assembly += '\n'

    def dump():
        file_content = HEADER + CodeGenerator.assembly + FOOTER
        return file_content

    