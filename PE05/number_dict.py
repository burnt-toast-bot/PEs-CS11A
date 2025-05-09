# define a function that takes a number as an argument
def create_dict(num):
    # creates an empty dictionary
    number_dict = {}

    # set the starting value equal to 1
    x = 1
    #while the number is less that the argument the loop will continue
    while x <= num:
        # add key, value pair equal to x and x squared
        number_dict[x] = x*x
        # goes to the next number in the sequence
        x += 1
    # returns the finished dictionary
    return number_dict

# asks user for a number to generate dictionary and prints the dictionary
print(create_dict(int(input("Enter a number: "))))