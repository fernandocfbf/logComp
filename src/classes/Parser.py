from src.classes.Token import Token
from src.classes.Tokenizer import Tokenizer
from src.constants.tokens import ALL_TOKENS, EXPRESSION_TOKENS, TERM_TOKENS

class Parser():
    tokens = None

    def parseFactor(tokenizer):
        '''
        input: Tokenizer object
        output: number (int)
        description: computes non-binary tokens (-, +)
        '''
        result = 0
        if tokenizer.actual.type == "number":
            result = int(tokenizer.actual.value)
            tokenizer.selectNext()
        elif tokenizer.actual.type == "+":
            tokenizer.selectNext()
            result += Parser.parseFactor(tokenizer)
        elif tokenizer.actual.type == "-":
            tokenizer.selectNext()
            result -= Parser.parseFactor(tokenizer)
        elif tokenizer.actual.type == "(":
            tokenizer.selectNext()
            result = Parser.parseExpression(tokenizer)
            if tokenizer.actual.type == ")":
                tokenizer.selectNext()
            else:
                raise Exception("Invalid syntax")
        else:
            raise Exception("Invalid expression")
        return result
        
    def parseTerm(tokenizer):
        '''
        input: Tokenizer object
        output: number (int)
        description: read all the tokens for the expression and calculates the result.
            Performs times and division only
        '''
        result = Parser.parseFactor(tokenizer)
        while tokenizer.actual.type in TERM_TOKENS:
            if tokenizer.actual.type == "*":
                tokenizer.selectNext()
                result *= Parser.parseFactor(tokenizer)
            elif tokenizer.actual.type == "/":
                tokenizer.selectNext()
                result /= Parser.parseFactor(tokenizer)
        return result

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
                tokenizer.selectNext()
                result += Parser.parseTerm(tokenizer)
            elif tokenizer.actual.type == "-":
                tokenizer.selectNext()
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
            if (begin != end) and (begin == -1 or end == -1):
                without_comments = True
                raise Exception("Invalid comment syntax")
            elif (begin != end):
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
        if(tokens.actual.type != "EOF"):
            raise Exception("Invalid syntax")
        return final_result
