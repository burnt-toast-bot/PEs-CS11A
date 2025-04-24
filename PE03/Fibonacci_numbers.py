#user inputs which position of Fibonacci number to generate
position = int(input("What position of Fibonacci numbers do you want to see? "))

count = 1                                   #starts loop at 1
fib_num1 = 0                                #Fib number position 1
fib_num2 = 1                                #Fib number position 2

if position == 1:                           #if asked for position 1 prints 0
    print(fib_num1)

while count <= position:                    #while counter is less than or equal to the position requested
    if count % 2 == 0:                      #if counter is even
        count += 1                          #update counter
        fib_num1 = fib_num1 + fib_num2      #update first Fib number to be next position
        if count == position:               #if at position print the current positions number
            print(fib_num1)
    else:                                   #if counter is odd
        count += 1                          #update counter
        fib_num2 = fib_num1 + fib_num2      #update update second Fib number to be the next position
        if count == position:               #if at position print the current positions number
            print(fib_num2)
    










