from src.constants.tokens import TOKENS
from Token import Token

class Tokenizer:
    def __init__(self, origin, position, actual):
        self.origin = origin #input (string) 
        self.position = position #current position (int)
        self.actual = actual #current token (Token)

    def selectNext(self):
        '''
        input: empty
        output: Token type object
        description: read the next token from the input and update the actual and position atributes
        '''
        current_token = self.origin[self.position]
        if current_token in TOKENS:
            self.position += 1
            self.actual = Token(TOKENS[current_token], "")
            return self.actual
        elif current_token.isnumeric():
            numero = current_token
            self.position += 1
            while (numero.isnumeric()):
                numero += self.origin[self.position]
                self.position += 1
        elif self.position >= len(self.origin):
            self.actual = Token("EOF", "")
        else:
            raise Exception("Character didn't recognize") 

