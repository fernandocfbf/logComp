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




