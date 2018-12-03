#Create variables
pop = int
time = int

#Introduce user to program
print("Aliens invaded Earth!")
print("In this simulation we can assume that aliens give birth to 1 new alien baby every week.")
print("We can also assume that a baby alien grows into an adult in a week.")
print("These aliens are also immortal.")
while True:
    #Ask for user input
    print("How many aliens landed on Earth?")
    pop = input()
    try:
        pop = int(pop)
        if pop >= 0:
            break
        else:
            print("This is a negative value, this program can only accept positive numbers.")
    except ValueError:
        print("The answer given is not a valid answer.")
    
while True:
    print("How long are they invading for? (In weeks)")
    time = input()
    try:
        time = int(time)
        if time >= 0:
            break
        else:
            print("This is a negative value, this program can only accept positive numbers.")
    except ValueError:
        print("The answer given is not a valid answer.")
    
        
if pop == 1:
    print("There is only 1 alien in week 0.")
else:
    print("In week 0 there are " + str(pop) + " aliens.")
for i in range(time):
    #Prints the population along with the week
    print("In week " + str(i + 1) + " there are " + str(pop * (2 ** (i + 1))) + " aliens.")

