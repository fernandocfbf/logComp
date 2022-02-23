class Parser():
    tokens = None

    def parseExpression(tokenizer):
        result = 0
        if tokenizer.actual.isnumeric():
            result = tokenizer.actual
            next_token = tokenizer.selectNext()

