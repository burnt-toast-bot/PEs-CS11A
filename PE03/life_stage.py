age = 3                             #set variable age

if age < 2:                         #if age is less than 2
    print("You are a baby!")
elif age >= 2 and age < 4:          #if age is at least 2 but less than 4
    print("You are a toddler!")
elif age >= 4 and age < 13:         #if age is at least 4 but less than 13
    print("You are a child.")
elif age >= 13 and age < 20:        #if age is at least 13 but less than 20
    print("You are a teenager.")
elif age >= 20 and age < 65:        #if age is at least 20 but less than 65
    print("You are an adult.")
else:                               #if age is at least 65
    print("You are an elder.")