# Akapit
paragraph = "cat dog mouse cat rat cat mouse"

# Rozdzielamy akapit na słowa za pomocą metody split()
words = paragraph.split()

# Tworzymy pusty słownik, który będzie przechowywał liczbę wystąpień każdego słowa
word_count = {}

# Iterujemy przez każde słowo w liście
for word in words:
    # Jeśli słowo już istnieje w słowniku, zwiększamy jego liczbę wystąpień
    if word in word_count:
        word_count[word] += 1
    else:
        # Jeśli słowo jeszcze nie istnieje w słowniku, dodajemy je z wartością 1
        word_count[word] = 1

# Wyświetlamy wynik
for word, count in word_count.items():
    print(f"{word}: {count}")
