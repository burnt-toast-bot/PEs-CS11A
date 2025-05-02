#creats a list of integers with duplicate elements
int_list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print(f"The list of integers is: {int_list}")

index = 0                           #starting index at position 0
dup_list = []                       #creates an empty list

while index < len(int_list):   #while the index is less than the length of the list
    num1 = int_list.pop(index) #removes the first value in the list and stores it in a variable
    if num1 in int_list:       #if the number is still in the integer list
        if num1 in dup_list:   #if the number is in our new list 
            continue           #program continues so we don't get duplicates in new list
        else:
            dup_list.append(num1) #otherwise add number to end of new list
    else:
        continue               #if number is not still in integer list, program continues
    index += 1                 #continues to the next index

print(f"The duplicate elements of the list of integers are: {dup_list}")
