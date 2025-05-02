#creates a tuple with five strings
simple_food = ("chicken strips", "rice", "meatloaf", "baked potatoe", "green beans")

for food in simple_food:    #for each string in tuple 
    print(food)             #print string

#simple_food.append("carrots") causes an error

#writes over simple_food tuple with updated values
simple_food = ("spaghetti", "rice", "meatload", "mashed potatoes", "green beans")

for food in simple_food:    #for each string in updated tuple
    print(food)             #print string