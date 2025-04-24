pattern = "*"                   #start of pattern

count = 1                       #counter starts at 1, will keep track of pattern
while count <= 5: #
    print(pattern.center(5))    #prints pattern centered
    pattern += "*"              #adds a * to pattern
    count += 1                  #adds to counter after adding to pattern
