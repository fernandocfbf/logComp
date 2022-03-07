from classes.Token import Token
from classes.Tokenizer import Tokenizer
from src.constants.tokens import TOKENS

class Parser():
    tokens = None

    def parseExpression(tokenizer):
        '''
        input: Tokenizer object
        output: number (int)
        description: read all the tokens for the expression and calculates the result 
        '''
        result = 0
        if tokenizer.actual.type == "number":
            result = tokenizer.actual
            next_token = tokenizer.selectNext() # Token object (type, value)
            while next_token.type in TOKENS:
                if next_token.type == '+':
                    next_token = tokenizer.selectNext()
                    if next_token.type == "number":
                        result += next_token.value # sum the token value
                    else:
                        raise Exception("Invalid syntax")
                elif next_token.type == '-':
                    next_token = tokenizer.selectNext()
                    if next_token.type == "number":
                        result -= next_token.value # subtract the token value
                    else:
                        raise Exception("Invalid syntax")
                next_token = tokenizer.selectNext()
            return result
        else:
            raise Exception("Invalid expression")
    
    def run(expression):
        '''
        input: expression with the operations to be performed (string)
        output: expression result (int)
        description: receives an expression in string format and calculates the result 
        '''
        tokens = Tokenizer(expression, -1, Token('number', 0))
        final_result = parseExpression(tokens)
        return final_result





