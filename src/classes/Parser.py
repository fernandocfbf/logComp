from src.classes.Token import Token
from src.classes.Tokenizer import Tokenizer
from src.constants.tokens import ALL_TOKENS, EXPRESSION_TOKENS, TERM_TOKENS

class Parser():
    tokens = None

    def parseTerm(tokenizer):
        '''
        input: Tokenizer object
        output: number (int)
        description: read all the tokens for the expression and calculates the result.
            Performs times and division only
        '''
        result = 0
        if tokenizer.actual.type == "number":
            result = int(tokenizer.actual.value)
            next_token = tokenizer.selectNext() # read operator
            while next_token.type in TERM_TOKENS:
                if next_token.type == "*":
                    next_token = tokenizer.selectNext()
                    if next_token.type == "number":
                        result *= int(next_token.value)
                    else:
                        raise Exception("Invalid syntax")
                elif next_token.type == "/":
                    next_token = tokenizer.selectNext()
                    if next_token.type == "number":
                        result /= int(next_token.value)
                    else:
                        raise Exception("Invalid syntax")
                next_token = tokenizer.selectNext()
            return result
        else:
            raise Exception("Invalid expression")

    def parseExpression(tokenizer):
        '''
        input: Tokenizer object
        output: number (int)
        description: read all the tokens for the expression and calculates the result.
            Performs sum and subtraction only 
        '''
        result = Parser.parseTerm(tokenizer)
        current_token = tokenizer.actual
        while current_token.type in EXPRESSION_TOKENS:
            if current_token.type == "+":
                current_token = tokenizer.selectNext()
                result += Parser.parseTerm(tokenizer)
            elif current_token.type == "-":
                current_token = tokenizer.selectNext()
                result -= Parser.parseTerm(tokenizer)

        return result
    
    def run(expression):
        '''
        input: expression with the operations to be performed (string)
        output: expression result (int)
        description: receives an expression in string format and calculates the result 
        '''
        tokens = Tokenizer(expression, 0, Token('number', expression[0]))
        tokens.selectNext()
        final_result = Parser.parseExpression(tokens)
        return final_result





