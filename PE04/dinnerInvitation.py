#creates a list with three strings
dinner_invite = ["JC", "Lauren", "Thea"]
print(dinner_invite)                    #prints the list

dinner_invite[2] = "Kayla"              #replaces the value at index 2
print(dinner_invite)                    #prints updated list

dinner_invite.insert(0, "Kenny")        #inserts a new value at the beginning of the list
dinner_invite.insert(2, "Robby")        #inserts a new value into the middle of the list (at index 2)
dinner_invite.append("Thea")            #adds a value to the end of the list
print(dinner_invite)                    #prints updated list

count = 0                               #defines a variable count which starts at 0

while count <= len(dinner_invite):      #while variable count is less than or equal to the length of the list
    no_invite = dinner_invite.pop()     #removes last value and stores it in variable no_invite
    #using variable no_invite prints a message apologizing for not inviting
    print(f"Sorry, {no_invite}, I can't invite you to dinner.") 
    count += 1                          #adds to the variable count

