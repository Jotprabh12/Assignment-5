words = input("Enter a list of words separated by spaces: ").split()
occurrences = {}

for word in words:
    if word in occurrences:
        occurrences[word] += 1
    else:
        occurrences[word] = 1

for word, count in occurrences.items():
    print(f"{word} occurs {count} times")