# Medical Calculators
#### Description:      
This is a GUI application with a **collection of tools/calculators commonly used on daily clinical practice** by medical professionals. 

I am a medical student, so I decided to create this program in order to avoid wasting time memorizing and applying common criteria, scores, and equations.


At the moment, this application includes the following calculators:
- **BMI Calculator**
- **CHA₂DS₂-VASc Score for Atrial Fibrillation Stroke Risk**
- **Creatinine Clearance formula (Cockcroft-Gault Equation)**


The GUI of this program was implemented using the library Tkinter.

There is two files in this project:
- project.py: this file contains the main code. I created multiple subclasses inheriting from tkinter frame class, each one representing a page with a different calculator/tool and also the main page. 
There is also a subclass of tkinter Tk, a toplevel widget that represents the window, where the frames are shown.
The file contains also several functions that do the calculations necessary in each medical calculator/tool.
- test_ptoject.py: this file is used to test the main code with pytest, through assertions.


# Usage
The program has a main page, where the user can choose the desired medical calculator from a dropdown menu. This will open the chosen calculator in the same window and prompt the user to entry the necessary values. The results will be displayed at the bottom after clicking on a "Enter" button.


# Thanks
Thanks to  David J. Malan and his team for making this incredible course freely available to everyone.
