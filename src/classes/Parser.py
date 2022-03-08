from src.classes.Token import Token
from src.classes.Tokenizer import Tokenizer
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
            next_token = tokenizer.selectNext() # read first number
            result = int(tokenizer.actual.value)
            next_token = tokenizer.selectNext() # read operator
            while next_token.type in TOKENS:
                if next_token.type == "+":
                    next_token = tokenizer.selectNext()
                    if next_token.type == "number":
                        result += int(next_token.value) # sum the token value
                    elif next_token.type != "space":
                        raise Exception("Invalid syntax")
                elif next_token.type == "-":
                    next_token = tokenizer.selectNext()
                    if next_token.type == "number":
                        result -= int(next_token.value) # subtract the token value
                    elif next_token.type != "space":
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
        expression = expression.replace(" ", "")
        tokens = Tokenizer(expression, 0, Token('number', expression[0]))
        final_result = Parser.parseExpression(tokens)
        return final_result





