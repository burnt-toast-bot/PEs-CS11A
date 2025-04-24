num = int(input("Please enter a number: "))  #user inputs number which is converted to an integer

count = 2                                   #checking if prime will start with number 2

while count <= num:                         #while numbers being checked are less than or equal to number entered
    if num % count == 0 and count != num:   #if number entered can be divided by current number and it is not equal to the number entered
        print(num, "is not a prime number") 
        break                               #not prime, ends loop
    elif num % count != 0:                  #if number entered can't be divided by current number
        count += 1                          #go to next number
        continue                            #continue loop                
    else:                                   #if count equals number entered and it has not been divisible by any number 
        print(num, "is a prime number") 
        break                               #is prime, ends loop
