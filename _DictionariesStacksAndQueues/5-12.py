def reverse_string(s):
    stack = []
    # Push each character onto the stack
    for char in s:
        stack.append(char)
    
    # Pop each character from the stack to reverse the string
    reversed_string = ''.join(stack[::-1])
    return reversed_string

text = input('Enter text to reverse: ')
reversed_text = reverse_string(text)
print(f"Reversed text: {reversed_text}")
