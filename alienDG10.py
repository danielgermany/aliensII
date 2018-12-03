#Create variables
pop = int
time = int
lifespan = int
prefWeek = int

#Introduce user to program
print("Aliens invaded Earth!")
print("In this simulation we can assume that aliens give birth to 1 new alien baby every week.")
print("We can also assume that a baby alien grows into adulthood in a week.")
print("These aliens are also immortal.")
while True:
    #Ask for user input
    print("How many aliens landed on Earth?")
    pop = input()
    #Attempts to make pop an int
    try:
        pop = int(pop)
        if pop >= 0:
            break
        else:
            print("This is a negative value, this program can only accept positive numbers.")
    except ValueError:
        print("The answer given is not a valid number.")

while True:
    print("How long are they invading for? (In weeks)")
    time = input()
    #Attempts to make time an int
    try:
        time = int(time)
        if pop >= 0:
            break
        else:
            print("This is a negative value, this program can only accept positive numbers.")
    except ValueError:
        print("The answer given is not a valid number.")
        
if pop == 1:
    print("There is only 1 alien in week 0.")
else:
    print("In week 0 there are " + str(pop) + " aliens.")
for i in range(time):
    #Prints the population along with the week
    print("In week " + str(i + 1) + " there are " + str(pop * (2 ** (i + 1))) + " aliens.")

print("Now lets assume that the aliens aren't immortal and they have a life span.")
while True:
    print("Enter a number to represent the lifespan of the aliens. (In weeks)")
    lifespan = input()
    try:
        lifespan = int(lifespan)
        if lifespan >= 0:
            break
        else:
            print("This is a negative value, this program can only accepts positive numbers")
    except ValueError:
        print("The answer given is not a valid number")
if pop == 1:
    print("There is only 1 alien in week 0.")
else:
    print("In week 0 there are " + str(pop) + " aliens.")
for a in range(time):
    if a <= lifespan:
        print("In week " + str(a + 1) + " there are " + str(pop * (2 ** (a + 1))) + " aliens.")
    else:
        print("In week " + str(a + 1) + " there are " + str(pop * (2 ** (a + 1)) - (pop * (2 ** ((a + 1) - lifespan)))) + " aliens.")
        print(str(pop * (2 ** ((a + 1) - lifespan))) + " aliens died this week")
print("You can now go back to a specific week you would like to observe.")
while True:
    #Ask for user input
    print("Enter the week you would like to observe.")
    prefWeek = input()
    #Attempts to make prefWeek an int
    try:
        prefWeek = int(prefWeek)
        if prefWeek > time:
            print("The week you choose is out of range. The aliens already left by then.")
        else:
            if prefWeek >= 0:
                if prefWeek <= lifespan:
                    print("In week " + str(prefWeek) + " there are " + str((pop * (2 ** prefWeek)))+ " aliens.")
                else:
                    print("In week " + str(prefWeek) + " there are " + str((pop * (2 ** prefWeek)) - (pop * (2 ** (prefWeek - lifespan))))  + " aliens.")
            else:
                print("This is a negative value, this program can only accept positive numbers.")
    except ValueError:
        print("The answer given is not a valid number.")

 
   



        
