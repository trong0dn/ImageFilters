""" T10_interactive_ui
Team identifier: 10
Contributing member(s):
    Trong Nguyen, 100848232
    Ahmed Abdellah, 101163588
    Karandev Andotra, 101141882
    Hussein Rashid, 101141962

Carleton University
ECOR 1051 Module 2 Project - Milestone 3
RELEASE = "April 2, 2020"
"""

from Cimpl import copy, load_image, save_as, show
from T10_user_interface import *

#-----------------------------------------------------------------
# Interactive User Interface Function

def interactive_ui() -> None:
    """ __author__ = "Trong Nguyen"
    
    Prompt the interactive user-interface.
    
    >>> interactive_ui()
    """
    prompts = ["L", "S", "2", "3", "X", "T", "P", "E", "I", "V", "H"]
    
    new_image = None
    on = True
    while on:
        command = get_command()  
        if command in prompts:
            if new_image:
                if command == "L":
                    new_image = load()
                else:   
                    new_image = execute_command(command, new_image)
                    show(new_image)
            else:
                if command == "L":
                    new_image = load()              
                else:
                    print("\t=> No image loaded\n")                                 
        elif command == "Q":
            on = False
        else:
            print("\t=> No such command\n")
            
#-----------------------------------------------------------------
# Interactive User Interface Main Script

if __name__ == "__main__":
    
    interactive_ui()