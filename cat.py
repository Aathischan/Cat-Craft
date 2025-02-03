"""Aathi Parthipan, ENG 1P13, 400567584, 2024-11-15"""
"""The Cat class shows a cat with attributes like name, health (hearts), and the number of fish in its stomach. It can be tame or wild, alive or dead. While feeding a cat can help it become healthier and even tame, overfeeding can kill it, and beating a cat will make it sicker and possibly even kill it. A `__str__` method is included in the class to show the cat's current status. The cat's fish count drops at the end of each night, and if it is tame and has fish, it leaves a present. Dead cats cannot be fed or given gifts."""

import random

class Cat:
    """This class records and manipulates the cat's objects, like the health xp, the fish count, alive/dead, tame/wild"""
    def __init__(self,name):
        """Sets the name of a new cat to its initial values. The cat's name (str) is one of the parameters. Attributes... name (str): The cat's name.cat_is_alive (bool): Defines if the cat is still alive. begins with "True." Whether the cat is wild is indicated by the cat_is_wild(bool) function. health (int): The cat's condition, beginning at 2. fish_count (int): The quantity of fish consumed by the cats, beginning at zero."""
        self.name = name
        # Cat starts off wild
        self.cat_is_wild = True
        # Cat is alive when born
        self.cat_is_alive = True
        # Cat health starts off with 2
        self.health = 2.00
        # Cat starts with 0 fish
        self.fish_count = 0
        
    def feed(self):
        """Gives the cat food. The cat's health improves and it may grow tame if it is alive and not overfed. The cat dies if it is overfed (more than three fish). This method changes the fish_count, tameness, and health of the cat."""
        # Create a list of tame or wild for later use
        tame_or_wild = ["tame", "wild"]
        
        # Check is cat is alive
        if not self.cat_is_alive:   
            raise Exception(f"{self.name} is not alive, therefore cannot be fed :(")
        
        # 1 fish = 1 health boost
        self.fish_count += 1
        self.health = min(self.health + 1, 4)
        feed = print(f"{self.name} has been fed and it's current health is : {self.health}")
      
        
        # Cat is dead if eats more than three fish
        if self.fish_count > 3:
            self.cat_is_alive = False
            self.health = 0
            return f"{self.name} has ate too much and died :("
        else:
            if random.choice(tame_or_wild) == "tame": 
                self.cat_is_wild = False
            else:
                self.cat_is_wild = True
        return feed 
    
    def hit(self):
        """Hitting the cat, causing it to become untamed and less healthy. The cat dies if its health drops to zero. The health and tameness of the cat are altered by this method."""
        # Check is cat is alive
        if not self.cat_is_alive:   
            raise Exception(f"{self.name} is not alive, therefore cannot be hit :(")
        
        # Health goes down by 1.5 each time
        self.health = max(self.health - 1.5, 0.0)
        # Becomes wild
        self.cat_is_wild = True
        hit = print(f"{self.name} has been hit... Current health: {self.health}")
        
        if self.health <= 0.00: 
            # Health resets to 0
            self.health = 0.00
            # Cat is dead
            self.cat_is_alive = False
            return f"Warning: {self.name} is not alive, therefore cannot be hit :("
        return hit
        
    def end_night(self): 
        """Night goes for the cat. It loses one fish if it has consumed any. The cat leaves a present if it is tame. It turns wild if it hasn't eaten."""
        
        # initialize gifts
        gifts = ["Chicken", "Mutton", "Raw Salmon", "Raw Cod", "Encanted book"]
        
        
        if self.fish_count > 0:
            self.health = max(self.health - 1.0, 0)
            self.fish_count = max(self.health - 1, 0)
            if self.cat_is_wild == False:
                # Random from list of gifts
                gift = random.choice(gifts)
                gift_statement = print(f"{self.name} has left you a gift... The gift is : {gift}....Enjoy!")
                return gift_statement
        
        else: 
            # Health resets to 0
            self.health = 0
            # Cat is dead
            self.cat_is_alive = False
            return f"{self.name} is not alive, health is reset."
               
    
    def __str__(self): 
        """returns back a string representation of the cat that includes its health, number of fish, tameness (wild or tame), and current status (living or dead)."""
        if self.cat_is_alive:
            state = "Alive"
        else:
            state = "Dead"
            
        if self.cat_is_wild:
            status = "Wild"
        else:
            status = "Tamed"
        
        return f" {self.name}'s State: {state} \n {self.name}'s Status: {status} \n {self.name}'s Health: {self.health} \n {self.name}'s Fish Count: {self.fish_count}"
        