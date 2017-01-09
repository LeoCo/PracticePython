#Create a program that asks the user to enter their name
#and their age. Print out a message addressed to them
#that tells them the year that they will turn 100 years old.


name = input("Enter you name: ")

age = int(input("Enter your age: "))

year = 100 - age + 2016

message = "My dear " + name + ", you will be 100 years old on " + str(year)

print(message)

#Extras

copies = int(input("How many copies do you want to print?: "))

message += "\n"

print(copies * message)