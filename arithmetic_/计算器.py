#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: willowj
# date: 2018-02-06 21:57:18
#



ope_prio = {"+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "(": 5,
            ")": 5,
            }

def do(op,x,y):
    x = int(x)
    y = int(y)
    if op == "+":
        return x+y
    if op == "-":
        return x-y
    if op=="*":
        return x*y
    if op == "/":
        return x/y

formulate = "1+5+9*(9-(8+7))+9/3"


operate = []
stack = []

for x in formulate:

    if x == "(":
        operate.append(x)
    elif x.isdigit():
        stack.append(x)
    elif x in ")+-*/":
        while operate and (ope_prio[x] <= ope_prio[operate[-1]] or x == ")"):
            op = operate.pop()
            if op == "(":
                if x == ")":
                    continue
                else:
                    operate.append(op)
                    break

            f2 = stack.pop()
            f1 = stack.pop()
            stack.append(do(op,f1,f2))

        if x != ")":
            operate.append(x)

    # print stack,operate,x

while operate:
    op = operate.pop()
    f2 = stack.pop()
    f1 = stack.pop()
    stack.append(do(op,f1,f2))




#----##->----------------------------------------
import pdb

formulate = "1+5+9*(9-(8+7))+9/3"

ope_prio = {"+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "(": 5,
            ")": 5
            }

stack= []
op_stack = []

for x in formulate:
    if x.isdigit():
        stack.append(x)
    else:
        while op_stack and (ope_prio[x] <= ope_prio[op_stack[-1]] or x ==")"):
            op = op_stack.pop()
            pdb.set_trace()
            if op == "(":
                if x == ")":
                    continue
                else:
                    operate.append(op)
                    break
            stack.append(op)

        pdb.set_trace()
        if x != ")":
            op_stack.append(x)
        print stack, op_stack
while op_stack:
    stack.append(op_stack.pop())

print ''.join(stack)
