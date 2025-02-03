"""Aathi Parthipan, ENG 1P13, 400567584, 2024-11-26"""
"""The cat_craft.py program's goal is to create a text-based menu that mimics user interaction with several `Cat` objects in the CatCraft game universe. Each cat's health, tameness, and fish count are affected by the user's activities, such as feeding, hitting, or passing a night, which are mirrored in the three distinct `Cat` objects that the software creates. As the view in the Model-View-Controller hierarchy, the program calls the `Cat` methods in response to user input and uses the `__str__` method to show the cat statuses without actually accessing or changing the internal state of the cat."""

# import class Cat from cat.py
from cat import Cat

def print_signature():
    """The purpose of this function is to display the name and other information to the user"""
    print("Aathi Parthipan")
    print("400567584, Engineering")
    print("COMPSCI 1MD3: Introduction to Programming")
    print("Sam Scott")
    print("Fall 2024")

def cat_image(cats):
    """ take number of cats and dsiplays a picture of a cat and it's iniatlized variables"""
    for i in range(len(cats)):
        print("""
     /\_/\\
    ( o.o )
     > ^ <
    """)
        print(f"{cats[i]}")

def main():
    """Function mimic how a user might interact with the cats in the CatCraft environment. This application should generate three distinct Cat objects and provide a menu interface for the user to interact with each one."""
    
    # Enter names for each cat
    cat1 = input("Enter the name of the first cat: ")
    cat2 = input("Enter the name of the second cat: ")
    cat3 = input("Enter the name of the third cat: ")
    
    # Initalize cats
    cats = [Cat(cat1), Cat(cat2), Cat(cat3)]
    
    while True: 
        # Display Cats
        cat_image(cats)
    
        # Give user choices
        print(" \n 1. Feed \n 2. Hit \n 3. Night Pass \n 4. Quit")
        choice = int(input("Please Enter You Choice: "))
        if choice <= 0 and choice > 4: 
                raise ValueError("Invalid Choice Number") 
        
        # auto quit when 4 is clicked
        if choice == 4:
            print("Thanks for playing Cat Craft!")
            break
        
        try: 
            # Run feed             
            if choice == 1:
                cat = int(input("Which cat would you like to feed? (1,2,3): ")) - 1
                cats[cat].feed()
                print("Purrr!")
                # Run hit
            elif choice == 2:
                cat = int(input("Which cat would you like to hit? (1,2,3): ")) - 1
                cats[cat].hit()
                print("Hisss!")
            # Night passes...
            elif choice == 3:
                for cat in  cats:
                    night = cat.end_night()
                    if night: 
                        print(night)
            else:
                print("Try Again")
        except ValueError:
            print("Invalid Input. Please Enter a number assigned to one of the cats!")


if __name__ == "__main__":
    print_signature()
    main()