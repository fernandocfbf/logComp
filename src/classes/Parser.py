from src.classes.Identifier import Identifier
from src.classes.Print import Print
from src.classes.BinOp import BinOp
from src.classes.UnOp import UnOp
from src.classes.NoOp import NoOp
from src.classes.IntVal import IntVal
from src.classes.Block import Block
from src.classes.Token import Token
from src.classes.Assignment import Assignment
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
        int_result = 0
        if tokenizer.actual.type == "number":
            int_result = int(tokenizer.actual.value)
            tokenizer.selectNext()
            return IntVal(int_result, [])
        elif tokenizer.actual.type == "+":
            tokenizer.selectNext()
            node = UnOp("+", [Parser.parseFactor(tokenizer)])
            return node
        elif tokenizer.actual.type == "-":
            tokenizer.selectNext()
            node = UnOp("-", [Parser.parseFactor(tokenizer)])
            return node
        elif tokenizer.actual.type == "(":
            tokenizer.selectNext()
            int_result = Parser.parseExpression(tokenizer)
            if tokenizer.actual.type == ")":
                tokenizer.selectNext()
                return int_result
            else:
                raise Exception("Invalid syntax")
        else:
            raise Exception("Invalid expression")
        
    def parseTerm(tokenizer):
        '''
        input: Tokenizer object
        output: number (int)
        description: read all the tokens for the expression and calculates the result.
            Performs times and division only
        '''
        node = Parser.parseFactor(tokenizer)
        while tokenizer.actual.type in TERM_TOKENS:
            if tokenizer.actual.type == "*":
                tokenizer.selectNext()
                node = BinOp("*", [node, Parser.parseFactor(tokenizer)])
            elif tokenizer.actual.type == "/":
                tokenizer.selectNext()
                node = BinOp("/", [node, Parser.parseFactor(tokenizer)])
        return node

    def parseExpression(tokenizer):
        '''
        input: Tokenizer object
        output: Node object (Node)
        description: read all the tokens for the expression and calculates the result.
            Performs sum and subtraction only 
        '''
        node = Parser.parseTerm(tokenizer)
        while tokenizer.actual.type in EXPRESSION_TOKENS:
            if tokenizer.actual.type == "+":
                tokenizer.selectNext()
                node = BinOp("+", [node, Parser.parseTerm(tokenizer)])
            elif tokenizer.actual.type == "-":
                tokenizer.selectNext()
                node = BinOp("-", [node, Parser.parseTerm(tokenizer)])
        return node

    def parseStatement(tokenizer):
        '''
        input: Tokenizer object
        output: Token object (Assignment, Print or NoOp)
        description: computes assignments and print functions
        '''
        if (tokenizer.actual.type == 'identifier'):
            identifier = Identifier(tokenizer.actual.value, [])
            tokenizer.selectNext()
            if (tokenizer.actual.type == "="):
                result = Parser.parseExpression(tokenizer)
                if (tokenizer.actual.type == ";"):
                    tokenizer.selectNext()
                    return Assignment(identifier.variant, [identifier, result])
                raise Exception("Missing type ;")
            raise Exception("Invalid syntax")
        if (tokenizer.actual.type == 'print'):
            tokenizer.selectNext()
            if (tokenizer.actual.type == ')'):
                tokenizer.selectNext()
                result = Parser.parseExpression()
                if (tokenizer.actual.type == ')'):
                    tokenizer.selectNext()
                    if (tokenizer.actual.type == ";"):
                        tokenizer.selectNext()
                        return Print('print', [result])
                    raise Exception("Missing type ;")
            raise Exception("Invalid syntax")
        elif (tokenizer.actual.type == ";"):
            tokenizer.selectNext()
            return NoOp("", [])
        raise Exception("Invalid syntax")
        
    def parseBlock(tokenizer):
        '''
        input: Tokenizer object
        output:
        description: reads { and } and prints the final result
        '''
        if tokenizer.actual.type == "{":
            tokenizer.selectNext() 
            block = Block("", list())
            while (tokenizer.actual.type != "}"):
                node = Parser.parseStatement(tokenizer)
                block.children.append(node)
            return block
        else:
            raise Exception("Invalid code syntax")


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
