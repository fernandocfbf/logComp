def split_op_and_num(string, operations):
    '''
    input: string (string) with the operations, operations (list<string>) with the calculations
    output: two lists, number and operations
    description: get all operations and numbers in order in a list
    '''
    res_op = list()
    res_num = list()
    current_number = ""
    for char in string:
        if char in operations:
            res_num.append(current_number) # add the current number
            res_op.append(char) 
            current_number = "" # reset string
        else:
            current_number += char
    res_num.append(current_number) # add the final number
    return [res_op, res_num] 
