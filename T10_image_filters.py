""" T10_image_filters
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

from Cimpl import choose_file, copy, create_color, create_image, \
                  get_color, get_width, get_height, save_as, set_color, \
                  show, load_image, Image

from simple_Cimpl_filters import grayscale

#-----------------------------------------------------------------
# Color filter functions 

def red_channel(original_image: Image) -> Image:
    """ Developed by Ahmed Abdellah, 101163588
    
    Return a filtered image from a user-selected original image.
    RBG code (r,0,0) where r is the original red pixel value.
    
    >>> red_channel(original_image)
    """
    new_image = copy(original_image)
    for pixel in original_image:
        x, y, (r, g, b) = pixel
        new_color = create_color(r, 0, 0)
        set_color(new_image, x, y, new_color)
    return new_image

def green_channel(original_image: Image) -> Image:
    """ Developed by Karandev Andotra, 101141882
    
    Return a filtered image from a user-selected original image.
    RBG code (0,g,0) where g is the original green pixel value.
    
    >>> green_channel(original_image)
    """ 
    new_image = copy(original_image)
    for pixel in original_image:
        x, y, (r, g, b) = pixel
        new_color = create_color(0, g, 0)
        set_color(new_image, x, y, new_color)
    return new_image

def blue_channel(original_image: Image) -> Image:
    """ Developed by Hussein Rashid, 101141962
    
    Return a filtered image from a user-selected original image.
    RBG code (0,0,b) where b is the original blue pixel value.
    
    >>> blue_channel(original_image)
    """ 
    new_image = copy(original_image)
    for pixel in original_image:
        x, y, (r, g, b) = pixel
        new_color = create_color(0, 0, b)
        set_color(new_image, x, y, new_color)
    return new_image
   
def combine(image1: Image, image2: Image, image3: Image) -> Image:
    """ Developed by Trong Nguyen, 100848232
    
    Return a new image that is a combination of the RGB components
    of the three user-selected input images.
    
    >>> combine(red_image, green_image, blue_image)
    """
    new_image = copy(image1)
    width = get_width(image1)
    height = get_height(image1)
    for x in range(width):
        for y in range(height):
            r1, g1, b1 = get_color(image1, x, y)
            r2, g2, b2 = get_color(image2, x, y)
            r3, g3, b3 = get_color(image3, x, y)
            new_color = create_color(r1+r2+r3, g1+g2+g3, b1+b2+b3)
            set_color(new_image, x, y, new_color)
    return new_image

#-----------------------------------------------------------------
# Filter functions 

def two_tone(original_image: Image, color1: str, color2: str) -> Image:
    """ Developed by Hussein Rashid, 101141962
        Reviewed by Trong Nguyen, 100848232
    
    Return a two-tone copy of an image from a user-selected original image
    and two color tone inputs.
        
    >>> original_image = load_image(choose_file())
    >>> two_tone_image = two_tone(original_image,"yellow","cyan")
    """
    new_image = copy(original_image)
    color_name = ["black", "white", "red", 
                  "lime", "blue", "yellow", 
                  "cyan", "magenta", "gray"]
    color_code = [(0, 0, 0), (255, 255, 255), (255, 0, 0), 
                  (0, 255, 0), (0, 0, 255), (255, 255, 0), 
                  (0, 255, 255), (255, 0, 255), (128, 128, 128)]    
    
    for i in range(9):
        if color1 == color_name[i]:
            color_tone1= color_code[i]
            new_color1 = create_color(color_tone1[0], 
                                      color_tone1[1], 
                                      color_tone1[2]) 
        elif color2 == color_name[i]:
            color_tone2= color_code[i]
            new_color2 = create_color(color_tone2[0], 
                                      color_tone2[1], 
                                      color_tone2[2])
    
    for pixel in original_image:
        x, y, (r, g, b) = pixel
        brightness = (r+g+b) // 3
        if brightness < 128:
            set_color(new_image, x, y, new_color1)
        elif brightness >= 128:
            set_color(new_image, x, y, new_color2)
    return new_image

def three_tone(original_image: Image, color1: str, color2: str, color3: str) \
        -> Image:
    """ Developed by Hussein Rashid, 101141962
        Reveiwed by Trong Nguyen, 100848232
    
    Return a three tone copy of an image from a user-selected original image
    and three color tone inputs.
        
    >>> original_image = load_image(choose_file())
    >>> three_tone_image = three_tone(original_image,"yellow","magenta","cyan")
    """
    new_image = copy(original_image)
    color_name = ["black", "white", "red", 
                  "lime", "blue", "yellow", 
                  "cyan", "magenta", "gray"]
    color_code = [(0, 0, 0), (255, 255, 255), (255, 0, 0), 
                  (0, 255, 0), (0, 0, 255), (255, 255, 0), 
                  (0, 255, 255), (255, 0, 255), (128, 128, 128)]    
    
    for i in range(9):
        if color1 == color_name[i]:
            color_tone1= color_code[i]
            new_color1 = create_color(color_tone1[0], 
                                      color_tone1[1], 
                                      color_tone1[2]) 
        elif color2 == color_name[i]:
            color_tone2= color_code[i]
            new_color2 = create_color(color_tone2[0], 
                                      color_tone2[1], 
                                      color_tone2[2]) 
        elif color3 == color_name[i]:
            color_tone3= color_code[i]
            new_color3 = create_color(color_tone3[0], 
                                      color_tone3[1], 
                                      color_tone3[2])            

    for pixel in original_image:
        x, y, (r, g, b) = pixel
        brightness = (r+g+b) // 3
        if brightness < 85:
            set_color(new_image, x, y, new_color1)
        elif brightness <= 170:
            set_color(new_image, x, y, new_color2)
        elif brightness > 170:
            set_color(new_image, x, y, new_color3)                      
    return new_image

def extreme_contrast(original_image: Image) -> Image:
    """ Developed by Ahmed Abdellah, 101163588
        Reviewed by Karandev Andotra, 101141882
    
    Return an extreme contrast filtered image from a user-selected original 
    image.
    
    >>> original_image = load_image(choose_file())
    >>> extreme_contrast_image = extreme_contrast(original_image)
    """
    new_image = copy(original_image)
    
    for pixel in original_image:
        x, y, (r, g, b) = pixel
        if r <= 127:
            r = 0
        elif r >= 128:
            r = 255
        if g <= 127:
            g = 0
        elif g >= 128:
            g = 255
        if b <= 127:
            b = 0
        elif b >= 128:
            b = 255
        new_color = create_color(r, g, b)
        set_color(new_image, x, y, new_color)
    return new_image

def sepia(original_image:Image) -> Image:
    """ Developed by Karandev Andotra, 101141882
        Reviewed by Hussein Rashid, 101141962
    
    Return a sepia tinted copy of an image from a user-selected image. 

    >>> original_image = load_image(choose_file())
    >>> sepia_image = sepia(new_image)
    """
    new_image = grayscale(original_image)
    for pixel in new_image:
        x, y, (r, g, b) = pixel
        brightness = (r+g+b) // 3
        if brightness < 63: #dark gray
            new_color = create_color(1.1*r, g, 0.9*b)
        elif brightness <= 191: #medium gray
            new_color = create_color(1.15*r, g, 0.85*b)
        elif brightness > 191: #light gray
            new_color = create_color(1.08*r, g, 0.93*b)
        set_color(new_image, x, y, new_color)         
    return new_image

def _adjust_component(component: int) -> int:
    """ Developed by Trong Nguyen, 100848232
        Reviewed by Ahmed Abdellah, 101163588
    
    Return the midpoint value of the quadrant in which an input component 
    lies as defined by the range of 0 to 255, inclusive in four equal-size 
    quadrants.

    >>> _adjust_component(r)
    """
    if component < 64:
        midpoint = 31
    elif component < 128:
        midpoint = 95
    elif component < 192:
        midpoint = 159
    else:
        midpoint = 223
    return midpoint

def posterize(original_image: Image) -> Image:
    """ Developed by Trong Nguyen, 100848232
        Reviewed by Ahmed Abdellah, 101163588
        
    Return a posterized copy of an image from a user-selected original image. 
    
    >>> original_image = load_image(choose_file())
    >>> posterize_image = posterize(original_image)
    """
    new_image = copy(original_image)
    for pixel in original_image:
        x, y, (r, g, b) = pixel
        midpoint_red = _adjust_component(r)
        midpoint_green = _adjust_component(g)
        midpoint_blue = _adjust_component(b)
        new_color = create_color(midpoint_red, midpoint_green, midpoint_blue)
        set_color(new_image, x, y, new_color)
    return new_image

def detect_edges(original_image: Image, threshold: int) -> Image:
    """ Developed by Karandev Andotra, 101141882
        Reviewed by Hussein Rashid, 101141962
    
    Return an edge detection modified copy of an image from a user-selected 
    original image and an input threshold value.
    
    >>> original_image = load_image(choose_file())
    >>> detect_edges_image = detect_edges(original_image, 10)
    """
    new_image = copy(original_image)
    width = get_width(original_image)
    height = get_height(original_image)    
    
    for x in range(width):
        for y in range(height):
            if not y == height-1:
                r, g, b = get_color(new_image, x, y)
                r_down, g_down, b_down = get_color(new_image, x, y+1)
                
                brightness = (r+g+b) // 3
                brightness_down = (r_down+g_down+b_down) // 3
                
                if abs(brightness - brightness_down) > threshold:
                    new_color = create_color(0, 0, 0)
                else:
                    new_color = create_color(255, 255, 255)
                set_color(new_image, x, y, new_color)
            else:
                new_color = create_color(255, 255, 255)
                set_color(new_image, x, y, new_color)
    return new_image

def detect_edges_better(original_image: Image, threshold: int) -> Image:
    """ Developed by Trong Nguyen, 100848232
        Reviewed by Ahmed Abdellah, 101163588
    
    Return an improved edge detection modified copy of an image from a 
    user-selected original image and an input threshold value.
    
    >>> original_image = load_image(choose_file())
    >>> detect_edges_better_image = detect_edges_better(original_image, 10)
    """
    new_image = copy(original_image)
    width = get_width(original_image)
    height = get_height(original_image)    
    
    for x in range(width):
        for y in range(height):    
            if not y == height-1 and not x == width-1:
                r, g, b = get_color(new_image, x, y)
                r_down, g_down, b_down = get_color(new_image, x, y+1)
                r_right, g_right, b_right = get_color(new_image, x+1, y)
                
                brightness = (r+g+b) // 3
                brightness_down = (r_down+g_down+b_down) // 3
                brightness_right = (r_right+g_right+b_right) // 3
                
                if abs(brightness - brightness_down) > threshold \
                or abs(brightness - brightness_right) > threshold:
                    new_color = create_color(0, 0, 0)
                else:
                    new_color = create_color(255, 255, 255)
                set_color(new_image, x, y, new_color) 
            else:
                new_color = create_color(255, 255, 255)
                set_color(new_image, x, y, new_color)       
        new_color = create_color(255, 255, 255)
        set_color(new_image, x, y, new_color)        
    return new_image

def flip_vertical(original_image: Image) -> Image:
    """ Developed by Hussein Rashid, 101141962
        Reviewed by Trong Nguyen, 100848232
    
    Return a vertically flipped copy of an image from a user-selected 
    original image.  
    
    >>> original_image = load_image(choose_file())
    >>> flip_vertical_image = flip_vertical(original_image)
    """
    new_image = copy(original_image)
    width = get_width(original_image)
    height = get_height(original_image)    
    
    for y in range(height):
        for x in range(width//2):
            color = get_color(new_image, x, y)
            color_x = get_color(new_image, width-x-1, y)
            set_color(new_image, x, y, color_x)
            set_color(new_image, width-x-1, y, color)
    return new_image

def flip_horizontal(original_image: Image) -> Image:
    """ Developed by Ahmed Abdellah, 101163588
        Reviewed by Karandev Andotra, 101141882
    
    Return a horizontally flipped copy of an image from a user-selected 
    original image.  
    
    >>> original_image = load_image(choose_file())
    >>> flip_horizontal_image = flip_horizontal(original_image)
    """
    new_image = copy(original_image)
    width = get_width(original_image)
    height = get_height(original_image)    
    
    for x in range(width):
        for y in range(height//2):
            color = get_color(new_image, x, y)
            color_y = get_color(new_image, x, height-y-1)
            set_color(new_image, x, y, color_y)
            set_color(new_image, x, height-y-1, color)
    return new_image

