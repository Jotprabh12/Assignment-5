size = 5

count = 0

for i in range(0,size):
    for j in range(0,i+1):
        print(chr(65 + count), end=" ")
        # changing charater
        count += 1
    print()