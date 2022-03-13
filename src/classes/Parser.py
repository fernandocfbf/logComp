from ast import parse
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
        while tokenizer.actual.type in EXPRESSION_TOKENS:
            if tokenizer.actual.type == "+":
                current_token = tokenizer.selectNext()
                result += Parser.parseTerm(tokenizer)
            elif tokenizer.actual.type == "-":
                current_token = tokenizer.selectNext()
                result -= Parser.parseTerm(tokenizer)
        return result


    def clean_comments(text):
        '''
        input: string to be cleaned
        output: string without comments
        description: clean all comments (/* /*)
        '''
        parse_text = text
        without_comments = False
        while without_comments == False:
            begin = int(parse_text.find("/*"))
            end = int(parse_text.find("*/"))
            if (begin != end):
                parse_text = parse_text.replace(parse_text[begin:end+2], "")
            else:
                without_comments = True
        return parse_text
    
    def run(expression):
        '''
        input: expression with the operations to be performed (string)
        output: expression result (int)
        description: receives an expression in string format and calculates the result 
        '''
        parse_expression = Parser.clean_comments(expression)
        tokens = Tokenizer(parse_expression, 0, Token(None, parse_expression[0]))
        tokens.selectNext()
        final_result = Parser.parseExpression(tokens)
        return final_result





