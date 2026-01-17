paragraph = "cat dog mouse cat rat cat mouse"

word_count = {}

words = paragraph.split()

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(f"'{word}' appears {count} times")
