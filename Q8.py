numbers = []
for i in range(10):
    numbers.append(int(input("Enter an integer: ")))

positive_numbers = []
negative_numbers = []
odd_numbers = []
even_numbers = []
occurrences = {}

for number in numbers:
    if number > 0:
        positive_numbers.append(number)
    elif number < 0:
        negative_numbers.append(number)
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
    if number in occurrences:
        occurrences[number] += 1
    else:
        occurrences[number] = 1

print("Positive Numbers:", positive_numbers)
print("Negative Numbers:", negative_numbers)
print("Odd Numbers:", odd_numbers)
print("Even Numbers:", even_numbers)
print("Occurrences:", occurrences)