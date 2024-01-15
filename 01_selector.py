"""
simply a random selector to tell me who to facetime! (deals with imports) .
"""
import random

my_friends = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hank", "Ivy", "Jack"]

def facetime_choice(name):
    return random.choice(name)

rando = facetime_choice(my_friends)
print(rando)