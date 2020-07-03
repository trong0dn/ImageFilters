""" T10_batch_ui
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

from Cimpl import copy, load_image, save_as
from T10_user_interface import execute_command

#-----------------------------------------------------------------
# Batch User Interface Main Script

if __name__ == "__main__":

    batch_file = open(input("Enter batch filename: "))
    
    for line in batch_file:
        items = line.strip().split()
        new_image = copy(load_image(items[0]))
        for i in range(len(items)-2):
            new_image = execute_command((items[i+2]), new_image, False)
            save_as(new_image, str(items[1]))
        
    batch_file.close()
    