#This code takes user input and evaluates if that height, in inches, is tall enough to ride a theme park ride.

#userInput
height = input("How tall are you (in inches)? ")

#Checking if the user input is valid
for var in height:
    if var.isdigit():
        continue
    else:
        print("Please use only numbers. Try again.")
        exit()

#Transforms the string from the user into a valid integer for comparing
userHeight = int(height)

#Checks if the user is too tall for the ride or if the user has smashed in random numbers (108 inches is 9 ft)
if  40 <= userHeight <= 108:
    congratulations = "Congratulations! At " + str(userHeight) + " inches, you can ride!"
    print(congratulations)
elif userHeight > 108:
    print("Are you sure you're that tall? Try again.")
else:
    print("Sorry. Due to safety concerns, you can't ride the attraction.")