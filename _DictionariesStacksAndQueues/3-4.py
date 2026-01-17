def decimal_to_binary(n):
    stack = []
    
    while n > 0:
        stack.append(n % 2)
        n //= 2
    
    binary_number = ''.join(map(str, stack[::-1]))
    return binary_number

number = 18
binary = decimal_to_binary(number)

print(f"Natural number: {number}")
print(f"Binary number: {binary}")
