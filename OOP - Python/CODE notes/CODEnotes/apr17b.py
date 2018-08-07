"""
This module uses stacks to determine if an arithmetic expression
(represented as a string) has balanced parentheses.
"""

from apr17a import Stack

def isbalanced(arith_expr):
    S = Stack()
    for c in arith_expr:
       if c == '(':
           S.push('(')
       elif c == ')':
           if S.empty():
               return False
           else:
               S.pop()
    if S.empty():
        return True
    else:
        return False



