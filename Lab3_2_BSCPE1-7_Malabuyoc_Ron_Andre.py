#Write a method in python will create two separate text files after reading the source text file named integers.txt that contains 20 integers. The first output file will be named double.txt containing the square of all even integers found in integers.txt and the second file will be named triple.txt containing the cube of all odd numbers found in the integers.txt.

Even = []
Odd = []
with open("integers.txt", "r") as file:
    for line in file:
        numbers = int(line)
        if numbers % 2 == 0:
            Even.append(numbers)
        else:
            Odd.append(numbers)

print(Even)
print(Odd)