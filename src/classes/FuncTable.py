

class FuncTable():
    functions = dict()

    def getFunction(function_name):
        if function_name in FuncTable.functions.keys():
            return (FuncTable.table[function_name]["type"], FuncTable.table[function_name]["function"])
        raise Exception("{0} is not a function".format(function_name))
    
    def createFunction(type, function_name, function):    
        if function_name in FuncTable.functions.keys():
            raise Exception("{0} is not a function".format(function_name))
        FuncTable.table[function_name] = {"type": type, "function": function}

