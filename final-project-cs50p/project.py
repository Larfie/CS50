"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

import tkinter as tk
import re


# global variables
TITLE_FONT = ("Calibri", 45, "bold")
BACKGROUND_COLOR = "#1bb193"
DARK_BLUE = "#0072CE"
LIGHT_BLUE = "#88CFF9"


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        self.container = tk.Frame(self)
        self.container.pack(side = "top", fill = "both", expand = True)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array
        self.frames = {}


        self.show_frame(MainPage)

    # function to display a frame passed as a parameter
    def show_frame(self, cont):
        frame = cont(self.container, self)
        frame.grid(row = 0, column = 0, sticky ="nsew")
        frame.tkraise()


# Main page layout with selection menu
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = BACKGROUND_COLOR)
        self.controller = controller
        self.dict_selection_frames = {
            "BMI": BmiFrame,
            "CHA₂DS₂-VASc Score for Atrial Fibrillation Stroke Risk": ChaDsVascScore,
            "Creatinine Clearance formula (Cockcroft-Gault Equation)": CreatinineClearance
            }

        # frame configuration
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)

        # changes window title
        self.controller.title("Medical Calculator")

        # label with title of the frame mainpage
        title_label = tk.Label(self, text = "MEDICAL CALCULATORS", font = TITLE_FONT, foreground = "white", background = BACKGROUND_COLOR)

        # putting the title
        title_label.grid(row = 0, column = 0, sticky="N", pady=25)

        # function to change frame based on the option chosen in the selection menu that is created after this function
        def selecting_frame(clicked):
            controller.show_frame(self.dict_selection_frames[clicked])


        # dropdown menu with options to open the calculators
        calculators = tk.StringVar(self)
        calculators.set("BMI") # default value
        selection_menu = tk.OptionMenu(self, calculators, *self.dict_selection_frames.keys(), command = selecting_frame)
        selection_menu.config(font="helvetica36", width=30, height=5, bg="white")
        selection_menu.grid(row = 1, column =0)


# second window frame for BMI
class BmiFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=BACKGROUND_COLOR)

        # frame configuration
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)

        # label with title of the frame
        label = tk.Label(self, text ="BMI Calculator", font = TITLE_FONT, foreground="white", background=BACKGROUND_COLOR)
        label.grid(row = 0, column = 0, columnspan=2)

        # return to main page button
        return_button = tk.Button(self, text="Main Page", relief="raised", command=lambda: controller.show_frame(MainPage), borderwidth=5, width=8, height=1, font="Helvetica24")
        return_button.grid(row=3, column=1, sticky="SE", padx=4, pady=4)

        # defines variables to store the values
        weight = tk.DoubleVar(value=1)
        height = tk.DoubleVar(value=1)

        # function to modify the label with the result of BMI calculation
        def bmi_check():
            result = bmi_formula(weight.get(), height.get())
            result_label["text"] = f"{result:.1f}"
            result_frame.grid(row=3, column=0, columnspan=2)

        # validate command to be used in the entries
        self.vcmd = (parent.register(validate), r'%P')

        # creates entries for the values to be used in the calculation
        form_frame = tk.Frame(self, bd=2, relief=tk.SOLID,padx=10, pady=10)

        weight_label = tk.Label(form_frame, text ="Weight (kg)", font="Helvetica50")
        weight_label.grid(row=1, column=0, sticky="NE", padx=10, pady=10)

        weight_entry = tk.Entry(form_frame, width=25, borderwidth=3, font="Helvetica50", textvariable=weight, validate="focusout", validatecommand=self.vcmd, invalidcommand= (parent.register(lambda: not_valid(self, weight_entry, "Invalid Input"))))
        weight_entry.grid(row=1, column=1, sticky="NW", padx=10, pady=10)

        height_label = tk.Label(form_frame, text ="Height (cm)", font="Helvetica50")
        height_label.grid(row=2, column=0, sticky="NE", padx=10, pady=10)

        height_entry = tk.Entry(form_frame, width=25, borderwidth=3, font="Helvetica50", textvariable=height, validate="focusout", validatecommand=self.vcmd, invalidcommand= (parent.register(lambda: not_valid(self, height_entry,"Invalid Input"))))
        height_entry.grid(row=2, column=1, sticky="NW", padx=10, pady=10)

        # result frame and ranges for bmi
        result_frame = tk.Frame(self, bd=2, relief=tk.SOLID,padx=10, pady=10)
        tk.Label(result_frame, text ="Your BMI:", font="Helvetica50").grid(row=0, column=0, padx=10, pady=10)
        result_label = tk.Label(result_frame, text ="", font="Helvetica50")
        result_label.grid(row=1, column=0, padx=10, pady=10)

        # creates button to submit values and calculate
        enter_button = tk.Button(form_frame, text="Enter", relief="raised", command=bmi_check, borderwidth=5, width=20, height=2, font="Helvetica24")
        enter_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # using grid on the form frame
        form_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


# third window frame for CHA₂DS₂-VASc Score for Atrial Fibrillation Stroke Risk
class ChaDsVascScore(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=BACKGROUND_COLOR)

        dict_calc_params = {
            "Age": [{"<65": 0, "65 - 74": 1, "≥75": 2}],
            "Sex": [{"Male": 0, "Female": 1}],
            "Congestive Heart Failure":[{"No": 0, "Yes": 1}],
            "Hypertension History": [{"No": 0, "Yes": 1}],
            "Stroke/TIA/Thromboembolism History": [{"No": 0, "Yes": 1}],
            "Vascular Disease History": [{"No": 0, "Yes": 1}],
            "Diabetes History": [{"No": 0, "Yes": 1}]
            }

        # main frame configuration
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.columnconfigure(0, weight=1)

        # title of the calculator
        label = tk.Label(self, text ="CHA₂DS₂-VASc Score for Atrial Fibrillation Stroke Risk", wraplength=900, font = TITLE_FONT, justify="center", foreground="white", background=BACKGROUND_COLOR)
        label.grid(row=0, column=0)

        # return to main page button
        return_button = tk.Button(self, text="Main Page", relief="raised", command=lambda: controller.show_frame(MainPage), borderwidth=5, width=8, height=1, font="Helvetica24")
        return_button.place(relx=0.90, rely=0.89, anchor=tk.CENTER)

        # form frame configuration
        form_frame = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        for x in range(0, len(dict_calc_params) + 1):
            form_frame.rowconfigure(x, weight=1)
        form_frame.columnconfigure(0, weight=1)
        form_frame.columnconfigure(1, weight=1)
        form_frame.columnconfigure(2, weight=1)
        form_frame.columnconfigure(3, weight=1)

        # creates entries for the values to be used in the calculation and inserts them in the form frame
        # uses the dictionary (dict_calc_params) to create in a for loop: the label, and the correspondent buttons and values
        # stores the selected value in a dict for each parameter used in the calculator
        self.dict_store_values = {}

        for k, x in zip(dict_calc_params.keys(), range(0, len(dict_calc_params))):
            self.dict_store_values[k] = tk.IntVar(value=0)


            tk.Label(form_frame, text=k, font=("helvetica", 14, "bold"), justify="left", foreground=DARK_BLUE).grid(row=x, column=0)
            if k == "Vascular Disease History":
                tk.Label(form_frame, text="(prior MI, peripheral artery disease, or aortic plaque)", font=("Helvetica", 10)).grid(row=x, column=0, sticky="s")

            for option, y in zip(dict_calc_params[k][0], range(0, len(dict_calc_params[k][0]))):
                choice_button = tk.Radiobutton(form_frame, text = option, font=("helvetica", 14), variable = self.dict_store_values[k],
                                value = dict_calc_params[k][0][option])
                choice_button.grid(row=x, column=1 + y, sticky="w")


        # function to get the score interpretation and change label's text
        def chadsvasc_score_check():
            score = sum([x.get() for x in self.dict_store_values.values()])
            sex = "female" if self.dict_store_values["Sex"] == 1 else "male"

            result_label1["text"] = f"Score: {score:.0f}"
            result_label2["text"] = f"{chadsvasc_score_analysis(score=score, sex=sex)['Therapy']}"


        # result frame
        result_frame = tk.Frame(self, bd=2, relief=tk.SOLID)
        result_label1 = tk.Label(result_frame, text="Score:", font=("Helvetica", 16))
        result_label2 = tk.Label(result_frame, text="", font=("Helvetica", 16))
        result_label1.grid(row=1, column=0, padx=10, pady=10)
        result_label2.grid(row=2, column=0)
        result_frame.grid(row=2, column=0, padx=10, pady=10)

        # submit button
        form_frame.rowconfigure(len(dict_calc_params) + 1, minsize=20)
        tk.Button(form_frame, text = "Enter", font=("helvetica", 20), background=LIGHT_BLUE, command=chadsvasc_score_check).place(relheight=0.08, relwidth=0.3, relx=0.5, rely=0.93, anchor=tk.CENTER)

        # using grid on the form frame
        form_frame.grid(row=1, column=0, sticky="nsew", pady=10, padx=30)



# fourth window frame for Creatinine Clearance formula
class CreatinineClearance(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=BACKGROUND_COLOR)

        # frame configuration 
        self.columnconfigure(0, weight=1)
        for row in range(0, 3):
            self.rowconfigure(row, weight=1)

        # title of the calculator
        label = tk.Label(self, text ="Creatinine Clearance formula (Cockcroft-Gault Equation)", wraplength=900, font = TITLE_FONT, justify="center", foreground="white", background=BACKGROUND_COLOR)
        label.grid(row=0, column=0)

        # return to main page button
        return_button = tk.Button(self, text="Main Page", relief="raised", command=lambda: controller.show_frame(MainPage), borderwidth=5, width=8, height=1, font="Helvetica24")
        return_button.place(relx=0.90, rely=0.89, anchor=tk.CENTER)

        # defines variables to store the values
        sex = tk.StringVar(value="male")
        age = tk.IntVar(value=1)
        weight = tk.DoubleVar(value=1)
        serum_creatinine = tk.DoubleVar(value=1)

        # form frame configuration
        form_frame = tk.Frame(self, highlightbackground="black", highlightthickness=2)

        for colum in range(0,3):
            form_frame.columnconfigure(colum, weight=0 if colum==0 else 1)
        for row in range(0, 5):
            form_frame.rowconfigure(row, weight=1)

        # validate command to be used in the entries
        self.vcmd = (parent.register(validate), '%P')

        # creates entries for the values to be used in the calculation and inserts them in the form frame
        tk.Label(form_frame, text="Sex", font=("helvetica", 14, "bold"), justify="left", foreground=DARK_BLUE).grid(row=0, column=0)
        choice_button = tk.Radiobutton(form_frame, text = "Male", font=("helvetica", 14), variable = sex, value = "male")
        choice_button.grid(row=0, column=2, sticky="we")
        choice_button = tk.Radiobutton(form_frame, text = "Female", font=("helvetica", 14), variable = sex, value = "female")
        choice_button.grid(row=0, column=1, sticky="we")       

        tk.Label(form_frame, text="Age", font=("helvetica", 14, "bold"), justify="left", foreground=DARK_BLUE).grid(row=1, column=0)
        age_entry = tk.Entry(form_frame, width=25, borderwidth=3, font="Helvetica50", textvariable=age, validate="focusout", validatecommand=self.vcmd, invalidcommand= (parent.register(lambda: not_valid(self, age_entry, "Invalid Input"))))
        age_entry.grid(row=1, column=1, columnspan=2)

        tk.Label(form_frame, text="Weight(kg)", font=("helvetica", 14, "bold"), justify="left", foreground=DARK_BLUE).grid(row=2, column=0)
        weight_entry = tk.Entry(form_frame, width=25, borderwidth=3, font="Helvetica50", textvariable=weight, validate="focusout", validatecommand=self.vcmd, invalidcommand=(parent.register(lambda: not_valid(self, weight_entry, "Invalid Input"))))
        weight_entry.grid(row=2, column=1, columnspan=2)

        tk.Label(form_frame, text="Creatinine(mg/dl)", font=("helvetica", 14, "bold"), justify="left", foreground=DARK_BLUE, padx=10).grid(row=3, column=0)
        creatinine_entry = tk.Entry(form_frame, width=25, borderwidth=3, font="Helvetica50", textvariable=serum_creatinine, validate="focusout", validatecommand=self.vcmd, invalidcommand=(parent.register(lambda: not_valid(self, creatinine_entry, "Invalid Input"))))
        creatinine_entry.grid(row=3, column=1, columnspan=2)

        form_frame.grid(row=1, column=0, sticky="ns", pady=10, padx=30)


        # fucntion to check creatinine clearance
        def creatinine_check():
            result_label2["text"] = f"{creatinine_clearance_formula(sex.get(), age.get(), weight.get(), serum_creatinine.get()):.0f} ml/min"

        # submit button
        form_frame.rowconfigure(4, minsize=20)
        tk.Button(form_frame, text = "Enter", font=("helvetica", 20), background=LIGHT_BLUE, command=creatinine_check).grid(row=4, column=0, columnspan=3)

        # result frame
        result_frame = tk.Frame(self, bd=2, relief=tk.SOLID)
        result_label1 = tk.Label(result_frame, text="Creatinine Clearance: ", font=("Helvetica", 16))
        result_label2 = tk.Label(result_frame, text="", font=("Helvetica", 16))
        result_label1.grid(row=1, column=0, padx=10, pady=10)
        result_label2.grid(row=2, column=0)
        result_frame.grid(row=2, column=0, padx=10, pady=10)

        # using grid on the form frame
        form_frame.grid(row=1, column=0, sticky="nsew", pady=10, padx=30)


def main():
    app = tkinterApp()
    app.geometry("860x800")
    app.mainloop()


def bmi_formula(weight, height):
    # weight in kilograms and height in centimeters

    return weight/((height/100)**2)


def creatinine_clearance_formula(sex, age, weight, serum_cr):
    # CrCl (male) = ([140-age] × weight in kg)/(serum creatinine × 72)
    # CrCl (female) = CrCl (male) × 0.85

    cr_cl = ((140-age) * weight) / (serum_cr * 72)
    if sex == "female":
        cr_cl *= 0.85

    return cr_cl


def chadsvasc_score_analysis(score, sex):
    if (score == 0 and sex == "male") or (score == 1 and sex == "female"):
        return {"Risk": "Low", "Therapy": "No anticoagulant therapy"}
    elif score == 1 and sex == "male":
        return {"Risk": "Medium", "Therapy": "Oral anticoagulant should be considered"}
    else:
        return {"Risk": "High", "Therapy": "Oral anticoagulant is recommended"}


def validate(entry_data):
    """
    Validate if the input is a positive number with or without decimal places
    """
    print(entry_data)
    if re.search("^(?:[1-9]\d*|0(?!(?:\.0+)?$))?(?:\.\d+)?$", entry_data):
        return True
    return False


def not_valid(target_win, target_entry, error_message):
    # Error message if the data is not valid
    print("Error")
    error_label = tk.Label(target_win, text=error_message, font="helvetica45", foreground="red", background="white")
    error_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    error_label.after(3000, lambda: error_label.destroy() )
    target_entry.delete(0, 'end')



if __name__=="__main__":
    main()
