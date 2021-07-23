from stack import Stack

def calculator(input):
    dict = {}
    dict['^'] = 4
    dict['*'] = 3
    dict['/'] = 3
    dict['+'] = 2
    dict['-'] = 2
    dict['('] = 1
    
    operand_stack = Stack()
    operands_stack = Stack()

    equation = list(input.split())

    for token in equation:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token.isnumeric():
            operands_stack.push(token)
        elif token == '(':
            operand_stack.push(token)
        elif token == ')':
            token = operand_stack.pop()
            while token != '(':
                   operands_stack.push(token)
                   token = operand_stack.pop()
        elif token == '+' or token == '-' or token == '/' or token == '*' or token == '^':
            while(not operand_stack.is_empty() and dict[operand_stack.peek()] >= dict[token]):
                token_2 = operand_stack.pop()
                operands_stack.push(token_2)
            operand_stack.push(token)


    while not operand_stack.is_empty():
        token_2 = operand_stack.pop()
        operands_stack.push(token_2)
   
    print(convert(operands_stack))

def convert(operands_stack):
    stack_holder = []
    list = []

    while not operands_stack.is_empty():
        token = operands_stack.pop()
        stack_holder.append((token))
    while stack_holder:
        token = stack_holder.pop()
        if token.isnumeric():
            list.append(token)

        else:
            op2 = list.pop()
            op1 = list.pop()
            if token == '^':
                op3 = int(op1) ** int(op2)
                list.append(op3)
            elif token == '*':
                op3 = int(op1) * int(op2)
                list.append(op3)
            elif token == '/':
                op3 = int(op1) / int(op2)
                list.append(op3)
            elif token == '+':
                op3 = int(op1) + int(op2)
                list.append(op3)
            elif token == '-':
                op3 = int(op1) - int(op2)
                list.append(op3)

    final_result = list.pop()
    print(final_result)
    return final_result

calculator("23 ^ 23")

