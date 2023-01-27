Start = int(input("Enter the start of range : "))
End = int(input("Enter the end of range : "))
Num = int(input("Enter the number : "))

for i in range (Start,End +1 ):
   if i % Num == 0:
    print (i)