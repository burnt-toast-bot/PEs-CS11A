import random  # Python Software Foundation (n.d.). Generate pseudo-random numbers. 
               # Python.org. https://docs.python.org/3/library/random.html

class Restaurant:
    
 # creates a class representing a restaurant
    
    def __init__(self, restaurant_name, cuisine_type, open):
        # initialize restaurant attributes; restaurant name and
        # cuisine type are strings and open is a boolean value
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open = open
    
    def describe_restaurant(self):
    # print a description of the restaurant
        if self.open == True:
            status = "open right now."
        else:
            status = "closed right now."
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()} "
               f"style cuisine. {self.restaurant_name.title()} is " + status)

    
    def is_open(self):
    # print whether the restaurant is open or closed
        if self.open == True:
            print("Currently open")
        else:
            print("Currently closed")
    
    def recommend(*restaurants):
        # create a list of open restaurants to recommend
        # from a tuple containing arbitrary number of restaurants
        yes_open = []
        for restaurant in restaurants:
            if restaurant.open == False:
                continue
            else: # if restaurant is open add to the end of the list
                yes_open.append(restaurant)
        return yes_open # returns list after looping through entire tuple

# create three instances of Restaurant
restaurant1 = Restaurant("In-n-Out", "Burgers and fries", True)
restaurant2 = Restaurant("Cafe Lago", "Italian", False)
restaurant3 = Restaurant("daniel's broiler", "seafood", True)

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# call recommend() to get list of open restaurants
opened = Restaurant.recommend(restaurant1, restaurant2, restaurant3)

# selects random restaurant from list of open restaurants
recommendation = random.choice(opened)

recommendation.describe_restaurant()
recommendation.is_open()