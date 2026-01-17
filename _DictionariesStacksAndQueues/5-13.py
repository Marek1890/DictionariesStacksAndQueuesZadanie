def evaluate_rpn(expression):
    stack = []
    for token in expression.split():
        if token.isdigit():  # If the token is a number, push it to the stack
            stack.append(int(token))
        elif token in '+-*/':  # If the token is an operator, pop two elements and apply the operation
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
        elif token == '=':  # If the token is '=', print the result
            return stack.pop()
    return None

expression = input("Enter RPN expression: ")
result = evaluate_rpn(expression)
print(f"Result: {result}")
