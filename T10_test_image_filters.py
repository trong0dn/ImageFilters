""" T10_test_image_filters
Team identifier: 10
Contributing member(s):
    Trong Nguyen, 100848232
    Ahmed Abdellah, 101163588
    Karandev Andotra, 101141882
    Hussein Rashid, 101141962

Carleton University
ECOR 1051 Module 2 Project - Milestone 2
RELEASE = "ImageFilters 1.0; March 26, 2020"
"""

from Cimpl import create_color, create_image, get_color, set_color
from unit_testing import check_equal
from T10_image_filters import *

#-----------------------------------------------------------------
# Filter test functions

def test_red() -> None:
    """ Developed by Ahmed Abdellah, 101163588
    
    Test whether red_channel function pass or fail.
    Check if the RGB values are (r,0,0) where r is the red pixel amount.
    
    >>> test_red()
    """
    
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(1, 0, 0))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(125, 73, 224))
    set_color(original, 4, 0,  create_color(254, 255, 255))
    set_color(original, 5, 0,  create_color(255, 255, 255))
    
    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(1, 0, 0))
    set_color(expected, 2, 0,  create_color(127, 0, 0))
    set_color(expected, 3, 0,  create_color(125, 0, 0))
    set_color(expected, 4, 0,  create_color(254, 0, 0))
    set_color(expected, 5, 0,  create_color(255, 0, 0))
    
    red_image = red_channel(original)
    
    for x, y, col in red_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                 col, get_color(expected, x, y))

def test_green() -> None:
    """ Developed by Karandev Andotra, 101141882
    
    Test whether green_channel function pass or fail.
    Check if the RGB values are (0,g,0) where g is the green pixel amount.
    
    >>> test_green()
    """
    
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 1, 0))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(125, 73, 224))
    set_color(original, 4, 0,  create_color(255, 254, 255))
    set_color(original, 5, 0,  create_color(255, 255, 255))
    
    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(0, 1, 0))
    set_color(expected, 2, 0,  create_color(0, 127, 0))
    set_color(expected, 3, 0,  create_color(0, 73, 0))
    set_color(expected, 4, 0,  create_color(0, 254, 0))
    set_color(expected, 5, 0,  create_color(0, 255, 0))
    
    green_image = green_channel(original)
    
    for x, y, col in green_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                 col, get_color(expected, x, y))
      
def test_blue() -> None:
    """ Developed by Hussein Rashid, 101141962
    
    Test whether blue_channel function pass or fail.
    Check if the RGB values are (0,0,b) where b is the blue pixel amount.
    
    >>> test_blue()
    """
    
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 0, 1))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(125, 73, 224))
    set_color(original, 4, 0,  create_color(255, 255, 254))
    set_color(original, 5, 0,  create_color(255, 255, 255))
    
    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(0, 0, 1))
    set_color(expected, 2, 0,  create_color(0, 0, 127))
    set_color(expected, 3, 0,  create_color(0, 0, 224))
    set_color(expected, 4, 0,  create_color(0, 0, 254))
    set_color(expected, 5, 0,  create_color(0, 0, 255))
    
    blue_image = blue_channel(original)
    
    for x, y, col in blue_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                 col, get_color(expected, x, y))
   
def test_combine() -> None:
    """ Developed by Trong Nguyen, 100848232
    
    Test whether combine function pass or fail.
    
    >>> test_combine()
    """
    
    original_red = create_image(6, 1)
    set_color(original_red, 0, 0,  create_color(0, 0, 0))
    set_color(original_red, 1, 0,  create_color(1, 0, 0))
    set_color(original_red, 2, 0,  create_color(127, 0, 0))
    set_color(original_red, 3, 0,  create_color(125, 0, 0))
    set_color(original_red, 4, 0,  create_color(254, 0, 0))
    set_color(original_red, 5, 0,  create_color(255, 0, 0))
        
    original_green = create_image(6, 1)
    set_color(original_green, 0, 0,  create_color(0, 0, 0))
    set_color(original_green, 1, 0,  create_color(0, 1, 0))
    set_color(original_green, 2, 0,  create_color(0, 127, 0))
    set_color(original_green, 3, 0,  create_color(0, 73, 0))
    set_color(original_green, 4, 0,  create_color(0, 254, 0))
    set_color(original_green, 5, 0,  create_color(0, 255, 0))
    
    original_blue = create_image(6, 1)
    set_color(original_blue, 0, 0,  create_color(0, 0, 0))
    set_color(original_blue, 1, 0,  create_color(0, 0, 1))
    set_color(original_blue, 2, 0,  create_color(0, 0, 127))
    set_color(original_blue, 3, 0,  create_color(0, 0, 224))
    set_color(original_blue, 4, 0,  create_color(0, 0, 254))
    set_color(original_blue, 5, 0,  create_color(0, 0, 255))    
    
    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(1, 1, 1))
    set_color(expected, 2, 0,  create_color(127, 127, 127))
    set_color(expected, 3, 0,  create_color(125, 73, 224))
    set_color(expected, 4, 0,  create_color(254, 254, 254))
    set_color(expected, 5, 0,  create_color(255, 255, 255))
    
    combine_image = combine(original_red, original_green, original_blue)
    
    for x, y, col in combine_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                 col, get_color(expected, x, y))
        
def test_two_tone() -> None:
    """ Developed by Ahmed Abdellah, 101163588
        Reviewed by Karandev Andotra, 101141882
    
    Test whether two_tone function pass or fail.
    
    >>> test_two_tone()
    """
    
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(52, 37, 42))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(128, 128, 128))
    set_color(original, 4, 0,  create_color(125, 73, 224))
    set_color(original, 5, 0,  create_color(255, 255, 255))
    
    expected_wb = create_image(6, 1)
    set_color(expected_wb, 0, 0,  create_color(0, 0, 0))
    set_color(expected_wb, 1, 0,  create_color(0, 0, 0))
    set_color(expected_wb, 2, 0,  create_color(0, 0, 0))
    set_color(expected_wb, 3, 0,  create_color(255, 255, 255))
    set_color(expected_wb, 4, 0,  create_color(255, 255, 255))
    set_color(expected_wb, 5, 0,  create_color(255, 255, 255))
    
    expected_rl = create_image(6, 1)
    set_color(expected_rl, 0, 0,  create_color(255, 0, 0))
    set_color(expected_rl, 1, 0,  create_color(255, 0, 0))
    set_color(expected_rl, 2, 0,  create_color(255, 0, 0))
    set_color(expected_rl, 3, 0,  create_color(0, 255, 0))
    set_color(expected_rl, 4, 0,  create_color(0, 255, 0))
    set_color(expected_rl, 5, 0,  create_color(0, 255, 0))
    
    expected_by = create_image(6, 1)
    set_color(expected_by, 0, 0,  create_color(0, 0, 255))
    set_color(expected_by, 1, 0,  create_color(0, 0, 255))
    set_color(expected_by, 2, 0,  create_color(0, 0, 255))
    set_color(expected_by, 3, 0,  create_color(255, 255, 0))
    set_color(expected_by, 4, 0,  create_color(255, 255, 0))
    set_color(expected_by, 5, 0,  create_color(255, 255, 0))
    
    expected_cm = create_image(6, 1)
    set_color(expected_cm, 0, 0,  create_color(0, 255, 255))
    set_color(expected_cm, 1, 0,  create_color(0, 255, 255))
    set_color(expected_cm, 2, 0,  create_color(0, 255, 255))
    set_color(expected_cm, 3, 0,  create_color(255, 0, 255))
    set_color(expected_cm, 4, 0,  create_color(255, 0, 255))
    set_color(expected_cm, 5, 0,  create_color(255, 0, 255))
    
    expected_gb = create_image(6, 1)
    set_color(expected_gb, 0, 0,  create_color(128, 128, 128))
    set_color(expected_gb, 1, 0,  create_color(128, 128, 128))
    set_color(expected_gb, 2, 0,  create_color(128, 128, 128))
    set_color(expected_gb, 3, 0,  create_color(0, 0, 0))
    set_color(expected_gb, 4, 0,  create_color(0, 0, 0))
    set_color(expected_gb, 5, 0,  create_color(0, 0, 0))    
    
    two_tone_image = two_tone(original,"black", "white")
    for x, y, col in two_tone_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                 col, get_color(expected_wb, x, y))
    
    two_tone_image = two_tone(original,"red", "lime")
    for x, y, col in two_tone_image:   
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                 col, get_color(expected_rl, x, y))   
    
    two_tone_image = two_tone(original,"blue", "yellow")    
    for x, y, col in two_tone_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                 col, get_color(expected_by, x, y))
    
    two_tone_image = two_tone(original,"cyan", "magenta")    
    for x, y, col in two_tone_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                 col, get_color(expected_cm, x, y))
    
    two_tone_image = two_tone(original,"gray", "black")
    for x, y, col in two_tone_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                 col, get_color(expected_gb, x, y))
        
def test_three_tone() -> None:
    """ Developed by Ahmed Abdellah, 101163588
        Reviewed by Karandev Andotra, 101141882
    
    Test whether three_tone function pass or fail.
    
    >>> test_three_tone()
    """
    
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(80, 84, 88))
    set_color(original, 2, 0,  create_color(80, 85, 90))
    set_color(original, 3, 0,  create_color(150, 170, 190))
    set_color(original, 4, 0,  create_color(170, 171, 172))
    set_color(original, 5, 0,  create_color(255, 255, 255))
    
    expected_wbr= create_image(6, 1)
    set_color(expected_wbr, 0, 0,  create_color(0, 0, 0))
    set_color(expected_wbr, 1, 0,  create_color(0, 0, 0))
    set_color(expected_wbr, 2, 0,  create_color(255, 255, 255))
    set_color(expected_wbr, 3, 0,  create_color(255, 255, 255))
    set_color(expected_wbr, 4, 0,  create_color(255, 0, 0))
    set_color(expected_wbr, 5, 0,  create_color(255, 0, 0))
    
    expected_lby = create_image(6, 1)
    set_color(expected_lby, 0, 0,  create_color(0, 255, 0))
    set_color(expected_lby, 1, 0,  create_color(0, 255, 0))
    set_color(expected_lby, 2, 0,  create_color(0, 0, 255))
    set_color(expected_lby, 3, 0,  create_color(0, 0, 255))
    set_color(expected_lby, 4, 0,  create_color(255, 255, 0))
    set_color(expected_lby, 5, 0,  create_color(255, 255, 0))
    
    expected_cmg = create_image(6, 1)
    set_color(expected_cmg, 0, 0,  create_color(0, 255, 255))
    set_color(expected_cmg, 1, 0,  create_color(0, 255, 255))
    set_color(expected_cmg, 2, 0,  create_color(255, 0, 255))
    set_color(expected_cmg, 3, 0,  create_color(255, 0, 255))
    set_color(expected_cmg, 4, 0,  create_color(128, 128, 128))
    set_color(expected_cmg, 5, 0,  create_color(128, 128, 128))
    
    three_tone_image = three_tone(original,"black", "white", "red")
    for x, y, col in three_tone_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', 
                    col, get_color(expected_wbr, x, y))
    
    three_tone_image = three_tone(original,"lime", "blue", "yellow")
    for x, y, col in three_tone_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', 
                    col, get_color(expected_lby, x, y))
    
    three_tone_image = three_tone(original,"cyan", "magenta", "gray")
    for x, y, col in three_tone_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', 
                    col, get_color(expected_cmg, x, y)) 

def test_extreme_contrast() -> None:
    """ Developed by Hussein Rashid, 101141962
        Reviewed by Trong Nguyen, 100848232
        
    Test whether extreme_contrast function pass or fail.
    
    >>> test_extreme_contrast()
    """
    
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(127, 127, 127))
    set_color(original, 2, 0,  create_color(224, 73, 125))
    set_color(original, 3, 0,  create_color(125, 224, 73))
    set_color(original, 4, 0,  create_color(73, 125, 224))
    set_color(original, 5, 0,  create_color(255, 255, 255))
    
    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(0, 0, 0))
    set_color(expected, 2, 0,  create_color(255, 0, 0))
    set_color(expected, 3, 0,  create_color(0, 255, 0))
    set_color(expected, 4, 0,  create_color(0, 0, 255))
    set_color(expected, 5, 0,  create_color(255, 255, 255))
    
    extreme_contrast_image = extreme_contrast(original)
    for x, y, col in extreme_contrast_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                 col, get_color(expected, x, y))
        
def test_sepia() -> None:
    """ Developed by Trong Nguyen, 100848232
        Reviewed by Ahmed Abdellah, 101163588
    
    Test whether sepia function pass or fail.
    
    >>> test_sepia()
    """
    
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(1, 1, 1))
    set_color(original, 2, 0,  create_color(63, 63, 63))
    set_color(original, 3, 0,  create_color(191, 191, 191))
    set_color(original, 4, 0,  create_color(192, 192, 192))
    set_color(original, 5, 0,  create_color(255, 255, 255))
    
    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(1, 1, 0))
    set_color(expected, 2, 0,  create_color(72, 63, 53))
    set_color(expected, 3, 0,  create_color(219, 191, 162))
    set_color(expected, 4, 0,  create_color(207, 192, 178))
    set_color(expected, 5, 0,  create_color(255, 255, 237))
    
    sepia_image = sepia(original)
    for x, y, col in sepia_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                 col, get_color(expected, x, y))  

def test_posterize() -> None:
    """ Developed by Karandev Andotra, 101141882
        Reviewed by Hussein Rashid, 101141962
        
    Test whether posterize function pass or fail.
    
    >>> test_posterize()
    """
    
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(1, 1, 1))
    set_color(original, 2, 0,  create_color(63, 64, 127))
    set_color(original, 3, 0,  create_color(127, 128, 191))
    set_color(original, 4, 0,  create_color(191, 192, 255))
    set_color(original, 5, 0,  create_color(255, 255, 255))
    
    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(31, 31, 31))
    set_color(expected, 1, 0,  create_color(31, 31, 31))
    set_color(expected, 2, 0,  create_color(31, 95, 95))
    set_color(expected, 3, 0,  create_color(95, 159, 159))
    set_color(expected, 4, 0,  create_color(159, 223, 223))
    set_color(expected, 5, 0,  create_color(223, 223, 223))
    
    posterize_image = posterize(original)
    for x, y, col in posterize_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                 col, get_color(expected, x, y))

def test_detect_edges() -> None:
    """ Developed by Trong Nguyen, 100848232
        Reviewed by Karandev Andotra, 101141882
    
    Test whether detect_edges function pass or fail.
    
    >>> test_detect_edges()
    """
    
    original = create_image(6, 2)
    set_color(original, 0, 0,  create_color(0, 0, 0)) #brightness 0
    set_color(original, 1, 0,  create_color(255, 255, 255)) #brightness 255
    set_color(original, 2, 0,  create_color(224, 73, 125)) #brightness 140
    set_color(original, 3, 0,  create_color(251, 65, 62)) #brightness 126
    set_color(original, 4, 0,  create_color(52, 173, 142)) #brightness 122
    set_color(original, 5, 0,  create_color(0, 0, 0)) #brightness 0
    
    set_color(original, 0, 1,  create_color(0, 0, 0)) #brightness 0
    set_color(original, 1, 1,  create_color(255, 255, 255)) #brightness 255
    set_color(original, 2, 1,  create_color(102, 93, 225)) #brightness 140
    set_color(original, 3, 1,  create_color(52, 173, 142)) #brightness 122
    set_color(original, 4, 1,  create_color(251, 42, 37)) #brightness 110
    set_color(original, 5, 1,  create_color(255, 255, 255)) #brightness 255 
    
    expected = create_image(6, 2)
    set_color(expected, 0, 0,  create_color(255, 255, 255))
    set_color(expected, 1, 0,  create_color(255, 255, 255))
    set_color(expected, 2, 0,  create_color(255, 255, 255))
    set_color(expected, 3, 0,  create_color(255, 255, 255))
    set_color(expected, 4, 0,  create_color(0, 0, 0))
    set_color(expected, 5, 0,  create_color(0, 0, 0))
    
    set_color(expected, 0, 1,  create_color(255, 255, 255))
    set_color(expected, 1, 1,  create_color(255, 255, 255))
    set_color(expected, 2, 1,  create_color(255, 255, 255))
    set_color(expected, 3, 1,  create_color(255, 255, 255))
    set_color(expected, 4, 1,  create_color(255, 255, 255))
    set_color(expected, 5, 1,  create_color(255, 255, 255))    
    
    detect_edges_image = detect_edges(original, THRESHOLD)
    for x, y, col in detect_edges_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                 col, get_color(expected, x, y))
        
def test_detect_edges_better() -> None:
    """ Developed by Hussein Rashid, 101141962
        Reviewed by Karandev Andotra, 101141882
    
    Test whether detect_edges_better function pass or fail.
    
    >>> test_detect_edges_better()
    """
    
    original = create_image(6, 2)
    set_color(original, 0, 0,  create_color(0, 0, 0)) #brightness 0
    set_color(original, 1, 0,  create_color(255, 255, 255)) #brightness 255
    set_color(original, 2, 0,  create_color(224, 23, 125)) #brightness 124
    set_color(original, 3, 0,  create_color(251, 65, 62)) #brightness 126
    set_color(original, 4, 0,  create_color(52, 173, 142)) #brightness 122
    set_color(original, 5, 0,  create_color(0, 0, 0)) #brightness 0
    
    set_color(original, 0, 1,  create_color(0, 0, 0)) #brightness 0
    set_color(original, 1, 1,  create_color(255, 255, 255)) #brightness 255
    set_color(original, 2, 1,  create_color(102, 23, 225)) #brightness 124
    set_color(original, 3, 1,  create_color(52, 173, 142)) #brightness 122
    set_color(original, 4, 1,  create_color(251, 42, 37)) #brightness 110
    set_color(original, 5, 1,  create_color(255, 255, 255)) #brightness 255 
    
    expected = create_image(6, 2)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(0, 0, 0))
    set_color(expected, 2, 0,  create_color(255, 255, 255))
    set_color(expected, 3, 0,  create_color(255, 255, 255))
    set_color(expected, 4, 0,  create_color(0, 0, 0))
    set_color(expected, 5, 0,  create_color(255, 255, 255))
    
    set_color(expected, 0, 1,  create_color(255, 255, 255))
    set_color(expected, 1, 1,  create_color(255, 255, 255))
    set_color(expected, 2, 1,  create_color(255, 255, 255))
    set_color(expected, 3, 1,  create_color(255, 255, 255))
    set_color(expected, 4, 1,  create_color(255, 255, 255))
    set_color(expected, 5, 1,  create_color(255, 255, 255))    
    
    detect_edges_better_image = detect_edges_better(original, THRESHOLD)
    for x, y, col in detect_edges_better_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                 col, get_color(expected, x, y))
        
def test_flip_vertical() -> None:
    """ Developed by Ahmed Abdellah, 101163588
        Reviewed by Hussein Rashid, 101141962
    
    Test whether flip_vertical function pass or fail.
    
    >>> test_flip_vertical()
    """
    
    original = create_image(6, 2)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(125, 73, 224))
    set_color(original, 2, 0,  create_color(224, 23, 125))
    set_color(original, 3, 0,  create_color(251, 65, 62))
    set_color(original, 4, 0,  create_color(52, 173, 142))
    set_color(original, 5, 0,  create_color(255, 255, 255))
    
    set_color(original, 0, 1,  create_color(0, 0, 0))
    set_color(original, 1, 1,  create_color(253, 200, 90)) 
    set_color(original, 2, 1,  create_color(102, 23, 225))
    set_color(original, 3, 1,  create_color(52, 173, 142)) 
    set_color(original, 4, 1,  create_color(251, 42, 37)) 
    set_color(original, 5, 1,  create_color(255, 255, 255))
    
    expected = create_image(6, 2)
    set_color(expected, 0, 0,  create_color(255, 255, 255))
    set_color(expected, 1, 0,  create_color(52, 173, 142))
    set_color(expected, 2, 0,  create_color(251, 65, 62))
    set_color(expected, 3, 0,  create_color(224, 23, 125))
    set_color(expected, 4, 0,  create_color(125, 73, 224))
    set_color(expected, 5, 0,  create_color(0, 0, 0))
    
    set_color(expected, 0, 1,  create_color(255, 255, 255))
    set_color(expected, 1, 1,  create_color(251, 42, 37))
    set_color(expected, 2, 1,  create_color(52, 173, 142))
    set_color(expected, 3, 1,  create_color(102, 23, 225))
    set_color(expected, 4, 1,  create_color(253, 200, 90))
    set_color(expected, 5, 1,  create_color(0, 0, 0))    
    
    flip_vertical_image = flip_vertical(original)
    for x, y, col in flip_vertical_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                 col, get_color(expected, x, y))
        
def test_flip_horizontal() -> None:
    """ Developed by Karandev Andotra, 101141882
        Reviewed by Ahmed Abdellah, 101163588
        
    Test whether flip_horizontal function pass or fail.
    
    >>> test_flip_horizontal()
    """
    
    original = create_image(6, 2)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(125, 73, 224))
    set_color(original, 2, 0,  create_color(224, 23, 125))
    set_color(original, 3, 0,  create_color(251, 65, 62))
    set_color(original, 4, 0,  create_color(52, 173, 142))
    set_color(original, 5, 0,  create_color(255, 255, 255))
    
    set_color(original, 0, 1,  create_color(0, 0, 0))
    set_color(original, 1, 1,  create_color(253, 200, 90)) 
    set_color(original, 2, 1,  create_color(102, 23, 225))
    set_color(original, 3, 1,  create_color(52, 173, 142)) 
    set_color(original, 4, 1,  create_color(251, 42, 37)) 
    set_color(original, 5, 1,  create_color(255, 255, 255))
    
    expected = create_image(6, 2)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(253, 200, 90)) 
    set_color(expected, 2, 0,  create_color(102, 23, 225))
    set_color(expected, 3, 0,  create_color(52, 173, 142))
    set_color(expected, 4, 0,  create_color(251, 42, 37)) 
    set_color(expected, 5, 0,  create_color(255, 255, 255))
    
    set_color(expected, 0, 1,  create_color(0, 0, 0))
    set_color(expected, 1, 1,  create_color(125, 73, 224))
    set_color(expected, 2, 1,  create_color(224, 23, 125))
    set_color(expected, 3, 1,  create_color(251, 65, 62))
    set_color(expected, 4, 1,  create_color(52, 173, 142))
    set_color(expected, 5, 1,  create_color(255, 255, 255))    
    
    flip_horizontal_image = flip_horizontal(original)
    for x, y, col in flip_horizontal_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                 col, get_color(expected, x, y))        
     
#---------------------------------------------------
# Main Script

if __name__ == "__main__":
  
    test_red()
    test_green()
    test_blue()
    test_combine()
    test_two_tone()
    test_three_tone()
    test_extreme_contrast()
    test_sepia()
    test_posterize()
    THRESHOLD = 10; test_detect_edges()
    THRESHOLD = 10; test_detect_edges_better()
    test_flip_vertical()
    test_flip_horizontal()