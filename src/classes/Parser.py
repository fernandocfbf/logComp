from gzip import READ
from lib2to3.pgen2 import token
from src.classes.Identifier import Identifier
from src.classes.Print import Print
from src.classes.Scanf import Scanf
from src.classes.While import While
from src.classes.If import If
from src.classes.BinOp import BinOp
from src.classes.UnOp import UnOp
from src.classes.NoOp import NoOp
from src.classes.IntVal import IntVal
from src.classes.StrVal import StrVal
from src.classes.VarDec import VarDec
from src.classes.FuncDec import FuncDec
from src.classes.Block import Block
from src.classes.Token import Token
from src.classes.Assignment import Assignment
from src.classes.Tokenizer import Tokenizer
from src.constants.tokens import RELEXPRESSION_TOKENS, EXPRESSION_TOKENS, TERM_TOKENS

class Parser():
    tokens = None

    def parseFactor(tokenizer):
        '''
        input: Tokenizer object
        output: UnOp / IntVal / Identifier object
        description: computes non-binary tokens (-, +, (, !) and function scanf
        '''
        int_result = 0
        if tokenizer.actual.type == "number":
            int_result = int(tokenizer.actual.value)
            tokenizer.selectNext()
            return IntVal(int_result, [])
        elif tokenizer.actual.type == "string":
            str_result = str(tokenizer.actual.value)
            tokenizer.selectNext()
            return StrVal(str_result, [])
        elif tokenizer.actual.type == "identifier":
            identifier = Identifier(tokenizer.actual.value, [])
            tokenizer.selectNext()
            return identifier
        elif tokenizer.actual.type == "+":
            tokenizer.selectNext()
            node = UnOp("+", [Parser.parseFactor(tokenizer)])
            return node
        elif tokenizer.actual.type == "-":
            tokenizer.selectNext()
            node = UnOp("-", [Parser.parseFactor(tokenizer)])
            return node
        elif tokenizer.actual.type == "!":
            tokenizer.selectNext()
            node = UnOp("!", [Parser.parseFactor(tokenizer)])
            return node
        elif tokenizer.actual.type == "(":
            tokenizer.selectNext()
            int_result = Parser.relExpression(tokenizer)
            if tokenizer.actual.type == ")":
                tokenizer.selectNext()
                return int_result
            else:
                raise Exception("Invalid syntax")
        elif tokenizer.actual.value == "scanf":
            tokenizer.selectNext()
            if tokenizer.actual.type == "(":
                tokenizer.selectNext()
                if tokenizer.actual.type == ")":
                    tokenizer.selectNext()
                    return Scanf('scanf', [])
            raise Exception("Invalid syntax")
        else:
            raise Exception("Invalid expression")
        
    def parseTerm(tokenizer):
        '''
        input: Tokenizer object
        output: BinOp object
        description: performs times, division and && condition
        '''
        node = Parser.parseFactor(tokenizer)
        while tokenizer.actual.type in TERM_TOKENS:
            if tokenizer.actual.type == "*":
                tokenizer.selectNext()
                node = BinOp("*", [node, Parser.parseFactor(tokenizer)])
            elif tokenizer.actual.type == "/":
                tokenizer.selectNext()
                node = BinOp("/", [node, Parser.parseFactor(tokenizer)])
            elif tokenizer.actual.type == "&&":
                tokenizer.selectNext()
                node = BinOp("&&", [node, Parser.parseFactor(tokenizer)])
        return node

    def parseExpression(tokenizer):
        '''
        input: Tokenizer object
        output: BinOp object
        description: performs sum, subtraction and && 
        '''
        node = Parser.parseTerm(tokenizer)
        while tokenizer.actual.type in EXPRESSION_TOKENS:
            if tokenizer.actual.type == "+":
                tokenizer.selectNext()
                node = BinOp("+", [node, Parser.parseTerm(tokenizer)])
            elif tokenizer.actual.type == "-":
                tokenizer.selectNext()
                node = BinOp("-", [node, Parser.parseTerm(tokenizer)])
            elif tokenizer.actual.type == "||":
                tokenizer.selectNext()
                node = BinOp("||", [node, Parser.parseTerm(tokenizer)])
            elif tokenizer.actual.type == ".":
                tokenizer.selectNext()
                node = BinOp(".", [node, Parser.parseTerm(tokenizer)])
        return node

    def relExpression(tokenizer):
        '''
        input: Tokenizer object
        output: BinOp object
        description: performs ==, < and >
        '''
        node = Parser.parseExpression(tokenizer)
        while tokenizer.actual.type in RELEXPRESSION_TOKENS:
            if tokenizer.actual.type == "==":
                tokenizer.selectNext()
                node = BinOp("==", [node, Parser.parseExpression(tokenizer)])
            elif tokenizer.actual.type == "<":
                tokenizer.selectNext()
                node = BinOp("<", [node, Parser.parseExpression(tokenizer)])
            elif tokenizer.actual.type == ">":
                tokenizer.selectNext()
                node = BinOp(">", [node, Parser.parseExpression(tokenizer)])
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
                tokenizer.selectNext()
                result = Parser.relExpression(tokenizer)
                if (tokenizer.actual.type == ";"):
                    tokenizer.selectNext()
                    return Assignment(identifier.variant, [identifier, result])
                raise Exception("Missing type ;")
            else:
                raise Exception("Invalid syntax")
        if (tokenizer.actual.value == 'print'):
            tokenizer.selectNext()
            if (tokenizer.actual.type == '('):
                tokenizer.selectNext()
                result = Parser.relExpression(tokenizer)
                if (tokenizer.actual.type == ')'):
                    tokenizer.selectNext()
                    if (tokenizer.actual.type == ";"):
                        tokenizer.selectNext()
                        return Print('print', [result])
                    raise Exception("Missing type ;")
            raise Exception("Invalid syntax")
        if (tokenizer.actual.type == 'type'):
            currentType = tokenizer.actual.value
            tokenizer.selectNext()
            if (tokenizer.actual.type == 'identifier'):
                allIdent = [(currentType, tokenizer.actual.value)]
                tokenizer.selectNext()
                while (tokenizer.actual.type == ","):
                    tokenizer.selectNext()
                    if (tokenizer.actual.type == 'identifier'):
                        allIdent.append((currentType, tokenizer.actual.value))
                        tokenizer.selectNext()
                    else:
                        raise Exception("Invalid expression")
                if (tokenizer.actual.type == ";"):
                    tokenizer.selectNext()
                    return VarDec('vardec', allIdent)
                raise Exception("Missing type ;")
            raise Exception("Invalid expression")
        if(tokenizer.actual.value == 'while'):
            tokenizer.selectNext()
            if (tokenizer.actual.type == '('):
                tokenizer.selectNext()
                result = Parser.relExpression(tokenizer)
                if (tokenizer.actual.type == ')'):
                    tokenizer.selectNext()
                    stat = Parser.parseStatement(tokenizer)
                    return While('while', [result, stat])
            raise Exception("Invalid syntax")
        if(tokenizer.actual.value == 'if'):
            tokenizer.selectNext()
            if (tokenizer.actual.type == '('):
                tokenizer.selectNext()
                result = Parser.relExpression(tokenizer)
                if (tokenizer.actual.type == ')'):
                    tokenizer.selectNext()
                    stat1 = Parser.parseStatement(tokenizer)
                    if (tokenizer.actual.value == 'else'):
                        tokenizer.selectNext()
                        stat2 = Parser.parseStatement(tokenizer)
                        return If('if', [result, stat1, stat2])
                    return If('if', [result, stat1])
            raise Exception("Invalid syntax")
        if (tokenizer.actual.type == '{'):
            return Parser.parseBlock(tokenizer)
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
        block = Block("", list())
        if tokenizer.actual.type == "{":
            tokenizer.selectNext() 
            while (tokenizer.actual.type != "}"):
                node = Parser.parseStatement(tokenizer)
                block.children.append(node)
            tokenizer.selectNext()
            return block
        else:
            raise Exception("Invalid code syntax")

    def parseDeclaration(tokenizer):
        '''
        input: Tokenizer object
        output:
        description:
        '''
        funcDecObject = FuncDec("", list())
        if tokenizer.actual.type == 'type':
            currentType = tokenizer.actual.value
            tokenizer.selectNext()
            if (tokenizer.actual.type == 'identifier'):
                identifier = Identifier(tokenizer.actual.value, [])
                funcDecObject.children.append(VarDec('vardec', (currentType, identifier))) #function type and name
                tokenizer.selectNext()
                if (tokenizer.actual.type == '('):
                    tokenizer.selectNext()
                    if tokenizer.actual.type == 'type':
                        currentType = tokenizer.actual.value
                        tokenizer.selectNext()
                        if tokenizer.actual.type == 'identifier':
                            identifier = Identifier(tokenizer.actual.value, [])
                            funcDecObject.children.append(VarDec('vardec', (currentType, identifier)))
                            tokenizer.selectNext()
                            while (tokenizer.actual.type == ","):
                                tokenizer.selectNext()
                                if tokenizer.actual.type == 'type':
                                    currentType = tokenizer.actual.value
                                    tokenizer.selectNext()
                                    if tokenizer.actual.type == 'identifier':
                                        identifier = Identifier(tokenizer.actual.value, [])
                                        funcDecObject.children.append(VarDec('vardec', (currentType, identifier)))
                                        tokenizer.selectNext()
                    
                    if (tokenizer.actual.type == ')'):
                        funcDecObject.children.append(Parser.parseBlock())
                        return funcDecObject
        raise Exception("Invalid syntax")

                        
    def parseProgram(tokenizer):
        '''
        input: Tokenizer object
        output:
        description:
        '''
        

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
        input: 
        output: expression result (int)
        description: receives an expression in string format and calculates the result 
        '''
        cleaned_expression = Parser.clean_comments(expression)
        tokens = Tokenizer(cleaned_expression, 0, Token(None, cleaned_expression[0]))
        tokens.selectNext()
        final_result = Parser.parseBlock(tokens)
        if(tokens.actual.type != "EOF"):
            raise Exception("Invalid syntax")
        return final_result
