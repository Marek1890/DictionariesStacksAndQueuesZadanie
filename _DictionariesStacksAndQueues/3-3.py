def brackets_ok(expression):
    # Stos do przechowywania nawiasów
    stack = []
    
    # Mapowanie nawiasów zamykających na otwierające
    matching_brackets = {')': '(', '}': '{', ']': '['}
    
    # Przechodzimy po każdym znaku w wyrażeniu
    for char in expression:
        if char in '({[':  # Jeżeli napotkamy nawias otwierający
            stack.append(char)  # Dodajemy go na stos
        elif char in ')}]':  # Jeżeli napotkamy nawias zamykający
            if not stack:  # Jeśli stos jest pusty, to mamy błąd
                return False
            top = stack.pop()  # Pobieramy nawias z wierzchu stosu
            if top != matching_brackets[char]:  # Sprawdzamy, czy pasuje do nawiasu zamykającego
                return False
    
    # Na końcu, jeżeli stos jest pusty, to wszystkie nawiasy są poprawnie zamknięte
    return len(stack) == 0


expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"
expression2 = "[(2+3]/4)"
expression3 = "(2-3*4+(5/6)"

if brackets_ok(expression1):
    print("Expression 1: Brackets are correct.")
else:
    print("Expression 1: Brackets are not correct.")

if brackets_ok(expression2):
    print("Expression 2: Brackets are correct.")
else:
    print("Expression 2: Brackets are not correct.")

if brackets_ok(expression3):
    print("Expression 3: Brackets are correct.")
else:
    print("Expression 3: Brackets are not correct.")
