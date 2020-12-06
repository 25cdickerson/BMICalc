#Imports tkinter to create a window.
from tkinter import *
root=Tk()
root.title("BMI Calculator By Preston Dickerson")

#Creates Frames for items to go in.
topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

#Creates labels to display how the app works.
theLabel = Label(topFrame, text="Body Mass Index also called BMI is used in the health industry")
theLabel.pack()
theLabel2 = Label(topFrame, text="to measure how over or underweight you are.")
theLabel2.pack()
theLabel3 = Label(topFrame, text="An ideal BMI ranges between 18.5 and 24.9.")
theLabel3.pack()
theLabel4 = Label(topFrame, text="bmi = weight /(height^2)*703")
theLabel4.pack()
theLabel5 = Label(topFrame, text="This is an example of someone who used our app.")
labelExamplename = Label(topFrame, text="Name = Boi")
labelExamplename.pack()
labelExampleheight = Label(topFrame, text="Height(in) = 69")
labelExampleheight.pack()
labelExampleweight = Label(topFrame, text="Weight(lb) = 160")
labelExampleweight.pack()

#Creates and displays variables to further display how it works.
name = "Boi"
height_in = 69
weight_lb = 160
bmi = weight_lb / (height_in ** 2)*703
labelExamplelabel = Label(topFrame, text="Boi's BMI is:")
labelExamplelabel.pack()
labelExample = Label(topFrame, text=bmi)
labelExample.pack()

#Entry Boxes and Labels for Height
LabelWhatisyourHeight = Label(topFrame, text="What is your height in inches?")
LabelWhatisyourHeight.pack()
Height = StringVar()
EntryBoxHeight = Entry(topFrame, textvariable=Height)
EntryBoxHeight.pack()
LabelWhatisyourHeightLabel = Label(topFrame, text="inches")
LabelWhatisyourHeightLabel.pack()


#Entry Boxes and Labels for Weight
LabelWhatisYourWeight = Label(topFrame, text="What is you Weight in pounds?")
LabelWhatisYourWeight.pack()
Weight = StringVar()
EntryBoxWeight = Entry(topFrame, textvariable=Weight)
EntryBoxWeight.pack()
LabelWhatisYourWeightLabel = Label(topFrame, text="pounds")
LabelWhatisYourWeightLabel.pack()

#Creates A Space
LabelNothing = Label(topFrame, text = "")
# Calculation Button (Figure out how to link this to a function
bmi = StringVar()
bmi.set("")
bmitwo = StringVar()
bmitwo.set("")


#Calculation Button (Figure out how to link this to a function
def calculate():
    pounds = float(Weight.get())
    inches = float(Height.get())
    # labelYourBMI = Label(topFrame, text="Your BMI is")
    bmi.set("Your BMI is")
    labelYourBMI = Label(topFrame, text=bmi)
    labelYourBMI.pack()
    bmitwo = (pounds) / (inches) ** 2 * 703
    labelYourBMI2 = Label(topFrame, text=bmitwo)
    labelYourBMI2.pack()
    return

ButtonCalculate = Button(topFrame, text="Calculate", command=calculate)
ButtonCalculate.pack()

def reset():
    # labelYourBMI2 = Button(topFrame, text="")
    bmi.set("")
    bmitwo.set("")
    Height.set('')
    Weight.set('')
    return



ButtonReset = Button(topFrame, text="Reset", command=reset)
ButtonReset.pack()
root.mainloop()




