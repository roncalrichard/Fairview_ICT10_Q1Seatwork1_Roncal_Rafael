from pyscript import display

# Variables
name = "Rafael Roncal"
age = 16
height = 167  
# More variables
display(f"Name: {name}", target="output")
display(f"Age: {age}", target="output")
display(f"Height: {height} cm", target="output")

# Lists!!!!!
cities = ['New York', 'Seattle', 'Naples']
display(f"Cities: {cities}", target="output")

# Boolean 
is_student = False 

# Dictionary
user_profile = {
    "color": "lake placid blue",
    "car_brand": "Subaru",
    "shoe_size": 10,
    "best_friend": "Jazzmaster Guitar"
}
display(f"Profile: {user_profile}", target="output")

# Set
fruits_set = {'apples', 'pinapples', 'mandarins', 'kiwis'}
display(f"Fruits Set: {fruits_set}", target="output")

# Tuple
(monday, tuesday, wednesday, thursday, friday) = range(5)
