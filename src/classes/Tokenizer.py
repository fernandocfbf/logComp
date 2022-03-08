from src.constants.tokens import TOKENS
from src.classes.Token import Token

class Tokenizer:
    def __init__(self, origin, position, actual):
        self.origin = origin #input (string) 
        self.position = position #current position (int)
        self.actual = actual #current token (Token)

    def selectNext(self):
        '''
        input: empty
        output: Token type object (self.actual)
        description: read the next token from the input and update the actual and position atributes
        '''
        if self.position >= len(self.origin):
            self.actual = Token("EOF", "")
            return self.actual
        current_token = self.origin[self.position]
        if current_token in TOKENS:
            self.position += 1
            self.actual = Token(TOKENS[current_token], "")
        elif current_token.isnumeric():
            number = current_token
            self.position += 1
            if (self.position < len(self.origin)):
                while (self.origin[self.position].isnumeric()):
                    number += self.origin[self.position]
                    self.position += 1
                    if self.position >= len(self.origin):
                        break
            self.actual = Token("number", number)
        else:
            raise Exception("Character didn't recognize")

        print('self ', self.actual.value) 
        return self.actual

 