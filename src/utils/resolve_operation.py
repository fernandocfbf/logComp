def resolve_operation(ops, nums):
    '''
    input: two lists, ops (operations +, - ...) and nums (int)    
    output: the operations result (int)
    description: calculates the operations in order 
    '''
    result = int(nums[0])
    for index in range(len(ops)):
        op = ops[index]

        if op == "+":
            result += int(nums[index+1])
        else:
            result -= int(nums[index+1])
    return result
     
        