#Use len(Length) function to print the length of the string.
x = input("")
print(len(x)) #This will count the spaces as well.

#Printing the string length without the spaces
x = x.replace(" ","")
print(len(x))