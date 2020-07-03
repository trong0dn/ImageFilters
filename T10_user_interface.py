""" T10_user_interface
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

from Cimpl import choose_file, copy, load_image, save_as, show, Image
from T10_image_filters import *    

#-----------------------------------------------------------------
# User Interface Functions

def get_command() -> str:
    """ __author__ = "Trong Nguyen"
    
    Prompt the user for a valid command and return the command input as
    uppercase.
    
    >>> get_command()
    """
    command = input(
        "L)oad image  S)ave-as" 
        "\n2)-tone  3)-tone  X)treme contrast  T)int sepia  P)osterize"
        "\nE)dge detect  I)mproved edge detect  V)ertical flip  H)orizontal flip"
        "\nQ)uit \n\n: ")
    command = command.upper() 
    return command

def load() -> Image:
    """ __author__ = "Trong Nguyen"
    
    Return a copy of a new image from a user-selected loaded image file.
    
    >>> load()
    """
    filename = choose_file()
    original_image = load_image(filename)
    new_image = copy(original_image) 
    return new_image

def execute_command(command: str, new_image: Image, threshold=True) -> Image:
    """ __author__ = "Trong Nguyen"
    
    Return a new image given a valid command, an image and if required, 
    a threshold value.
    
    >>> execute_command("E", new_image, 10)    
    """
    functions = {"L": load, "S": save_as,
                 "2": two_tone, "3": three_tone, 
                 "X": extreme_contrast, "T": sepia, "P": posterize, 
                 "E": detect_edges, "I": detect_edges_better,
                 "V": flip_vertical, "H": flip_horizontal}
    
    if command == "S":
        save_as(new_image, input("Enter new filename: "))
    elif command == "2":
        tone1 = "yellow"
        tone2 = "cyan"        
        new_image = two_tone(new_image, tone1, tone2)
    elif command == "3":
        tone1 = "yellow"
        tone2 = "magenta"
        tone3 = "cyan"
        new_image = three_tone(new_image, tone1, tone2, tone3)
    elif command == "E":
        if threshold:
            threshold = int(input("Enter threshold value: "))
        else:
            threshold = 10
        new_image = detect_edges(new_image, threshold)
    elif command == "I":
        if threshold:
            threshold = int(input("Enter threshold value: "))
        else:
            threshold = 10
        new_image = detect_edges_better(new_image, threshold)            
    elif functions[command]:
        new_image = functions[command](new_image)      
    else:
        print("\t=> No such command\n")               
    return new_image
