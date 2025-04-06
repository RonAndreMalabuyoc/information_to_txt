#Write a method in python will create two separate text files after reading the source text file named integers.txt that contains 20 integers. The first output file will be named double.txt containing the square of all even integers found in integers.txt and the second file will be named triple.txt containing the cube of all odd numbers found in the integers.txt.

Even = []
Odd = []
with open("integers.txt", "r") as file:
    print(file.read())

    for line in file:
        if file.read %2 == 0:
            Even.append(line)
        elif file.read %2 != 0:
            Odd.append(line)

print(Even)
print(Odd)