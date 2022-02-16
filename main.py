from os import remove
from posixpath import split
import sys

# constants
from src.general.constants import OPERATIONS

# created functions
from src.utils.remove_blanks import remove_blanks
from src.utils.split_op_and_num import split_op_and_num
from src.utils.resolve_operation import resolve_operation


operation = sys.argv[1]
trimm = remove_blanks(operation)
ops, nums = split_op_and_num(trimm, OPERATIONS)
result = resolve_operation(ops, nums)
if result != None:
    print(result)

