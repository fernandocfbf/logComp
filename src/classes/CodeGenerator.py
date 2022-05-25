from src.constants.asm import HEADER, FOOTER

class CodeGenerator:
    assembly = str()

    def write(code):
        CodeGenerator.assembly += code 
        CodeGenerator.assembly += '\n'

    def dump(file_name):
        file_content = HEADER + CodeGenerator.assembly + FOOTER
        print(file_name)
        with open(file_name, 'w') as file:
            file.write(file_content)
    