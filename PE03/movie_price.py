age = int(input("How old are you? "))   #lets user enter their age

if age < 3:                             #if age entered is less than 3 ticket is free
    print("Your ticket is free!")
elif age >= 3 and age <= 12:            #if age entered is between 3 and 12 ticket is $10
    print("That will be $10.")
else:                                   #if age entered is over 12 ticket is $15            
    print("That will be $15.")