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
    
    def recommend(self, *restaurants):
        for restaurant in restaurants:
            if restaurant.open == True:
                return restaurant
            else:
                continue


restaurant1 = Restaurant("In-n-Out", "Burgers and fries", True)
restaurant2 = Restaurant("Cafe Lago", "Italian", False)
restaurant3 = Restaurant("daniel's broiler", "seafood", False)

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

opened = Restaurant.recommend(restaurant1, restaurant2, restaurant3)

opened.describe_restaurant()
opened.is_open()