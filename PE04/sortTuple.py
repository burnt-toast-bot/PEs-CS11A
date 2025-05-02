#creates a list of tuples
tuple_list = [('452', 10), ('256', 5), ('100', 20), ('135', 15)]

def second(list):       #defines a function that takes a list as an argument
    return list[1]      #returns the second element

def sort_list(tuples):  #defines a function that takes tuples as an argument
    return sorted(tuples, key=second)   #returns the tuples sorted by the 
                                        #second element using the functions 
                                        #second()

print(sort_list(tuple_list)) #calls the function sort_list() giving the 
                             #list of tuples as an argument and prints
                             #the sorted list

#Reference: 
#Nguyen, K. (2020). CS 11A: Technology & Computing Components H0S04 
#Lists, Tuples and Strings (p. 6). School of Technology and Computing (STC).