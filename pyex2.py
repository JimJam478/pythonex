def evaluate(string):
    stack = []
    accepted = "1234567890+-/*"
    for i in string:
        if i not in accepted:
            return False
        elif i in ['+','-','*','/']:
            op1 = stack.pop()
            op2 = stack.pop()
            if i == '+':
                stack.append(op2+op1)
            elif i =='-':
                stack.append(op2-op1)
            elif i == '*':
                stack.append(op2*op1)
            elif i == '/':
                stack.append(op2//op1)
    
        else:
            stack.append(int(i))
                
    return stack.pop()

print(evaluate("234+"))
