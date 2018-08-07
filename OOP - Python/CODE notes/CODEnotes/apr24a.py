"""
This module contains a function that uses stacks to evaluate an 
arithmetic expression (represented as a string). The function returns 
result of the evaluation.

The following assumptions are made about the arithmetic expression:

(1) It is fully parenthesized (that is, there are parentheses around 
    every pair of operands to which an operator is to be applied).
(2) All numbers in the expression are single digits.
(3) There are no negative numbers in the expression.
(4) The only arithmetic operators in the expression are +, -, *, and /.
"""

from apr17a import Stack

def evaluate(arith_expr):
    digits = Stack()
    opers = Stack()
    for c in arith_expr:
        if c.isdigit():
            digits.push(c)
        elif c in "+-*/":
            opers.push(c)
        elif c == ")":
            op = opers.pop()
            firstnum = int(digits.pop())
            secondnum = int(digits.pop())
            if op == '+':
                digits.push(firstnum + secondnum)
            elif op == '-':
                digits.push(secondnum - firstnum)
            elif op == '*':
                digits.push(firstnum * secondnum)                
            elif op == '/':
                    digits.push(secondnum/firstnum)
    return digits.pop()

