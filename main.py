from os import remove
import sys

#created functions
from src.utils.remove_blanks import remove_blanks
from utils.split_op_and_num import split_op_and_num

operation = sys.argv[1]
trimm = remove_blanks(operation)

print("trimm -> ", trimm)

