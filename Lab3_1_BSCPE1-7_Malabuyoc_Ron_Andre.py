#Write a method in python to write multiple line of text contents into a text file mylife.txt

##While true loop to make sure for another input
while True:
    try:
##Input to put in text file
        my_file_input = input("Please put in you're personal details, Please: ")

        with open ("mylife.txt", "a") as file:
            file.write(my_file_input + "\n")
            print("Appended to mylife.txt")
##check for another input
        Another = input("Will you like to put more of your personal information in? y/n ")
        if Another == "n":
            break
    except:
        print("Let's do this again shall we.")

print("Appended to mylife.txt")