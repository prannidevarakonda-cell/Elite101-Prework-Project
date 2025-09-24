print("Welcome to the Pi Cafe Chatbot!")
name = input("Please enter your name: ")

# Convert age to an integer
age = int(input("Hello " + name + ", what is your age? "))

if age < 13:
    kids_menu = input("What would you like on the kids menu? ")
    print("Great choice! We'll bring you the " + kids_menu + ".")
else:
    normal_menu = input("What would you like to order? ")
    print("Excellent! We'll prepare your " + normal_menu + ".")
