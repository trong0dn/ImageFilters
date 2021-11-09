# ImageFilters
[Version 1.0] <br>
07/04/2020

-----------------------------------------------------------------------------
## CONTACT INFORMATION

Contact Name:		Trong Nguyen <br>
Affiliation: 		Carleton University - Systems and Computer Engineering <br>

-----------------------------------------------------------------------------
## DESCRIPTION

- ImageFilters is a Python application for RGB image manipulation using 
filters. The user will be able to load an image and then perform a sequence of
cumulative filters on this image. The resulting photo will be displayed after
that filter has been applied to the current photo.

- The application is composed of five files:
	T10_interactive_ui.py 		(interactive user-interface)
	T10_batch_ui.py 		(batch user-interface)
	T10_user_interface.py 		(script for batch and interactive UI)
	T10_image_filters.py 		(main script for filters)
	T10_test_image_filters.py 	(script for testing fitlers)

![filtered](https://user-images.githubusercontent.com/55768917/121969773-fb256680-cd42-11eb-87a1-be67d6938f23.jpg)

-----------------------------------------------------------------------------
## INSTALLATION

This program has only been tested for Windows 10 and macOS.

-------------------------- Installation Dependencies -------------------------

The application should work with Python 3.7 or later versions and require a 
few third-party Python modules. Below are the dependencies required for the 
toolset with the version with which the application was tested upon:
	* Python 3.8.1
	* Pillow 2.2.1
	* Cimpl 1.04

Supplementary libraries and testing file with modular dependencies.

	Cimpl.py 		(Carleton Image Manipulation Python Library)
	unit_testing.py		(required in T10_test_image_filters.py)
	simple_Cimpl_filters.py	(required in T10_image_filters.py)

---------------------------- Windows Installation ----------------------------

Open Command Prompt Window. Navigate and confirm the directory of Python. 
Verify that the latest version of Python and PIP packages have been installed. 
If needed, install or update for the latest version.

There are Pillow binaries for Windows compiled for the matrix of supported 
Python in both 32 and 64-bit versions. These binaries have all of the 
optional libraries with some exceptions. In the Command Prompt Window, run:

	python -m pip install pip
	python -m pip install Pillow

Download the Cimpl.py and simple_Cimpl_filters.py package into same directory 
as main Python application program. Cimpl provides a collection of functions 
for manipulating digital images. Noted that ImageFilters application was 
developed and tested on Windows 10 OS using Python IDE Wing 101 v7.2.1 from 
Wingware.

----------------------------- macOS Installation -----------------------------

Open Terminal (Applications/Terminal). Navigate and confirm the directory of 
Python. Verify that the latest version of Python and PIP package is installed. 
If needed, install or update for the latest version. In Terminal, run:

	get-pip.py

There are Pillow binaries for macOS compiled for the matrix of supported 
Python. These binaries have all of the optional libraries with some 
exceptions. To ensure that the PIP package and Pillow are installed at the 
correct location. In Terminal, run:

	python3 -m pip install pip
	python3 -m pip install Pillow

Verify that both packages are up-to-date or install the latest upgrade.
 
	pip3 install --upgrade pip
	pip3 install --upgrade Pillow

It is optional to install Xcode, which is another IDE and allows for 
“Building” on macOS. After installation, you will be prompted to install the 
Xcode Command Line Tools. In Terminal, run:
      
	xcode-select –install
	sudo easy_install pip
	sudo pip install pillow
	pip3.4 install pillow

Download the Cimpl.py and simple_Cimpl_filters.py package into same directory 
as main Python application program. Cimpl provides a collection of functions 
for manipulating digital images. Noted that ImageFilters application was 
developed and tested on Windows 10 OS using Python IDE Wing 101 v7.2.1 from 
Wingware.

macOS has reported some issues with the Cimpl function choose_file. This 
error commonly arises due to the import tkinter module within Cimpl, which 
provides a Python interface to the third-party Tk GUI toolkit. Hence, errors 
such as hanging file-open dialog box and error messages appearing in the 
Python shell the window appears to be caused by Tk interacting with macOS. 
Instead of porting Cimpl to a different GUI toolkit, which involves 
installing additional libraries. macOS users can call the input function 
instead of the choose_file to obtain an image file.

	filename = input('Enter the name of an image file: ') 
	image = load_image(filename)

Additionally, the batch user-interface will only function if the batch file 
that is created on TextEdit (macOS’ equivalent of Notepad) is formatted to 
plain text.

-----------------------------------------------------------------------------
## USAGE

------------------------- Interactive User-Interface -------------------------

In order to run the interactive user-interface, the user may wish to run it 
directly in the Python IDE. However, alternatively the user can also run the 
program in the Command Prompt Window. Open the Command Prompt Window and 
navigate the directory of Python.

	> python T10_interactive_ui.py

The interactive user-interface prompts the user with the following menu 
selection for valid command entries within the Python shell command. When 
prompted, enter a valid command.

	L)oad image  S)ave-as
	2)-tone  3)-tone  X)treme contrast  T)int sepia  P)osterize
	E)dge detect  I)mproved edge detect  V)ertical flip  H)orizontal flip
	Q)uit

	: 

Valid prompts selected prior to loading an image will raise an error message 
stating:

	=> No image loaded

Otherwise, non-existing prompts will raise an error message stating:

	=> No such command

Thus for the application to move forward the only option is to load the 
image with the command "L" which prompts the user to select an image file 
for a window pop-up menu to load. Only after an image is loaded is when 
the other valid commands are executable. The filters are applied cumulatively.
Note that there are no error handling in place for when the prompt to select
image is not completed. The program is raise an error and terminate the
program if the user does not select a valid image file.

Filters such as two_tone and three_tone have additional arguments which can 
be rendered with a sub-prompt, however, hard-code values have been used for 
simplicity. Where two_tone used "yellow" for dark pixel tones and "cyan" 
for bright pixel tone. Likewise, three_tone was hard-coded for "yellow" for 
dark pixel tones, "magenta" for mid-range brightness pixel tones, and "cyan" 
for bright pixel tones.

Filters such as detect_edges and detect_edges_better have additional 
arguments for the threshold value. There are no error control, if a
non-integer value is input, the program terminates. It should be noted that 
the user must enter a number, as the error handling for this parameter was 
not implemented rigorously. In the interactive user-interface, after 
loading an image, then entering the command "E" or "I" will prompt the 
user to:

	Enter threshold value: 

The user may wish to save the image by entering the command "S" which
executes the save_as function, which will prompt the user:

	Enter new filename: 

It should be mentioned that the filename must have an appropriate extension.
The supported image file formats are:'.bmp', '.gif', '.jpg', '.jpeg', '.png', 
'.tif', and '.tiff'.

The interactive user-interface may be terminate by entering the quite command 
"Q" in order to exit the application. 

---------------------------- Batch User-Interface ----------------------------

In order to run the batch user-interface, the user may wish to run it 
directly in the Python IDE. However, alternatively the user can also run the 
program in the Command Prompt Window. Open the Command Prompt Window and 
navigate the directory of Python.

	> python T10_batch_ui.py

The batch user-interface which takes a .txt file and runs through a series of 
filters and saves the image as a new image file. The program will prompt the 
user to enter a batch filename with the file extension.

The layout of the batch file takes in the first item as the filename, 
assuming there is an image stored in the same folder as this script with the 
given name and saves a new image file with the filename listed as the second 
item after a series of cumulative filter functions have been applied using 
valid commands. The entries of the batch file may look like this:
 
	miss_sullivan.jpg test1.jpg 2 X P
	miss_sullivan.jpg test2.jpg  V H

Note that the filter application for two_tone and three_tone have been 
hard-coded which preset color tones. In addition, the detect_edges and 
detect_edges_better have also been hard-coded with the threshold value of 10 
for simplicity and ease-of-use.

-----------------------------------------------------------------------------
## CREDITS

Thanks to the support of TAs and Instructors during the development of this
application.

---------------------------- Function Development ----------------------------

The following members have contributed to the development and revision of the
scripts for application:

Trong Nguyen 
	combine
	_adjust_component
	posterize
	detect_edges_better
	test_combine
	test_sepia
	test_detect_edges
	interactive_ui
	batch_ui
	user_interface

Ahmed Abdellah	
	red_channel
	extreme_contrast
	flip_horizontal
	test_red
	test_two_tone
	test_three_tone
	test_flip_vertical

Karandev Andotra		
	green_channel
	sepia
	detect_edges
	test_green
	test_posterize
	test_flip_horizontal

Hussein Rashid
	blue_channel
	two_tone	
	three_tone
	flip_vertical
	test_blue
	test_extreme_contrast
	test_detect_edges_better		

-----------------------------------------------------------------------------
## LICENSE

[MIT](https://choosealicense.com/licenses/mit/)

Copyright (c) 2020 Trong Nguyen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
