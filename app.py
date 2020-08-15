import tkinter as tk
from tkinter import *
import time
import sys

parent = tk.Tk()

formulaeWelcome = tk.Label(text = 'Welcome to the Math Formulae Finder')
formulaeWelcome.pack()

formulaeUsage = tk.Label(text = "Usage: Click your formula's category to find it.")
formulaeUsage.pack()

exitFormCalc = tk.Button(text = 'Exit', height = 4, width = 30, command = exit)
exitFormCalc.pack()

volPyrandConePicImg = tk.PhotoImage(file = '/Volumes/Samsung T5/Math Formulae Finder/images/cone.png')
volCylinderPicImg = tk.PhotoImage(file = '/Volumes/Samsung T5/Math Formulae Finder/images/cylinder.png')
volSpherePicImg = tk.PhotoImage(file = '/Volumes/Samsung T5/Math Formulae Finder/images/sphere.png')
volRPrismPicImg = tk.PhotoImage(file = '/Volumes/Samsung T5/Math Formulae Finder/images/cuboid.png')
volPrismPicImg = tk.PhotoImage(file = '/Volumes/Samsung T5/Math Formulae Finder/images/prism.png')
volCubePicImg = tk.PhotoImage(file = '/Volumes/Samsung T5/Math Formulae Finder/images/cube.png')
volCubePic = tk.Button(image = volCubePicImg)
volPrismPic = tk.Button(image = volPrismPicImg)
volRPrismPic = tk.Button(image = volRPrismPicImg)
volSpherePic = tk.Button(image = volSpherePicImg)
volCylinderPic = tk.Button(image = volCylinderPicImg)
volPyrandConePic = tk.Button(image = volPyrandConePicImg)
geoEulerImg = tk.PhotoImage(file = '/Volumes/Samsung T5/Math Formulae Finder/images/Euler.png')
geoEqCircleImg = tk.PhotoImage(file = '/Volumes/Samsung T5/Math Formulae Finder/images/EqCircle.png')
geoDistTwoPtsImg = tk.PhotoImage(file = '/Volumes/Samsung T5/Math Formulae Finder/images/DistTwoPts.png')
geoEqPlaneImg = tk.PhotoImage(file = '/Volumes/Samsung T5/Math Formulae Finder/images/EqPlane.png')
geoEqSphereImg = tk.PhotoImage(file = '/Volumes/Samsung T5/Math Formulae Finder/images/EqSphere.png')
geoMidpointsImg = tk.PhotoImage(file = '/Volumes/Samsung T5/Math Formulae Finder/images/Midpoints.png')
geoSumIntAngImg = tk.PhotoImage(file = '/Volumes/Samsung T5/Math Formulae Finder/images/SumIntAng.png')
geoEqStrtLineImg = tk.PhotoImage(file = '/Volumes/Samsung T5/Math Formulae Finder/images/EqStrtLine.png')
geoEqEllipseImg = tk.PhotoImage(file = '/Volumes/Samsung T5/Math Formulae Finder/images/EqEllipse.png')
geoPyTheoremImg = tk.PhotoImage(file = '/Volumes/Samsung T5/Math Formulae Finder/images/PyTheorem.png')
funcandEqImg = tk.PhotoImage(file = '/Volumes/Samsung T5/Math Formulae Finder/images/FuncandEq.png')
trig1img = tk.PhotoImage(file = '/Volumes/Samsung T5/Math Formulae Finder/images/trig1.png')
trig2img = tk.PhotoImage(file = '/Volumes/Samsung T5/Math Formulae Finder/images/trig2.png')
trig3img = tk.PhotoImage(file = '/Volumes/Samsung T5/Math Formulae Finder/images/trig3.png')
trig1imgpic = tk.Button(image = trig1img)
trig2imgpic = tk.Button(image = trig2img)
trig3imgpic = tk.Button(image = trig3img)
geoEulerImgPic = tk.Button(image = geoEulerImg)
geoEqCircleImgPic = tk.Button(image = geoEqCircleImg)
geoDistTwoPtsImgPic = tk.Button(image = geoDistTwoPtsImg)
geoEqPlaneImgPic = tk.Button(image = geoEqPlaneImg)
geoEqSphereImgPic = tk.Button(image = geoEqSphereImg)
geoMidpointsImgPic= tk.Button(image = geoMidpointsImg)
geoSumIntAngImgPic = tk.Button(image = geoSumIntAngImg)
geoEqStrtLineImgPic = tk.Button(image = geoEqStrtLineImg)
geoEqEllipseImgPic = tk.Button(image = geoEqEllipseImg)
geoPyTheoremImgPic = tk.Button(image = geoPyTheoremImg)
funcandEqImgPic = tk.Button(image = funcandEqImg)

PyrandConeFormula = tk.Label(text = 'V = 1/3b x h')
CylinderFormula = tk.Label(text = 'V = πr^2 x h')
SphereFormula = tk.Label(text = 'V = 4/3πr^3')
RPrismFormula = tk.Label(text = 'V = l x w x h')
PrismFormula = tk.Label(text = 'V = b × h')
CubeFormula = tk.Label(text = 'V = s^3')

def ifDoneVolButtonClick():
    SphereFormula.pack_forget()
    PyrandConeFormula.pack_forget()
    PrismFormula.pack_forget()
    CylinderFormula.pack_forget()
    CubeFormula.pack_forget()
    RPrismFormula.pack_forget()
    volCubePic.pack_forget()
    volPrismPic.pack_forget()
    volSpherePic.pack_forget()
    volCylinderPic.pack_forget()
    volRPrismPic.pack_forget()
    volPyrandConePic.pack_forget()
    menuEntry.pack()
    volCube.pack()
    volRPrism.pack()
    volPrism.pack()
    volPyrandCone.pack()
    volSphere.pack()
    volCyl.pack()
    doneVolButton.pack_forget()

def ifDoneGeoButtonClick():
    geoEulerImgPic.pack_forget()
    geoEqCircleImgPic.pack_forget() 
    geoDistTwoPtsImgPic.pack_forget()
    geoEqPlaneImgPic.pack_forget() 
    geoEqSphereImgPic.pack_forget()
    geoMidpointsImgPic.pack_forget()
    geoSumIntAngImgPic.pack_forget()
    geoEqStrtLineImgPic.pack_forget()
    geoEqEllipseImgPic.pack_forget()
    geoPyTheoremImgPic.pack_forget()
    menuEntry.pack()
    geoEulerButton.pack()
    geoSumIntAngButton.pack()
    geoPyTheoremButton.pack()
    geoDistTwoPtButton.pack()
    geoMidPtButton.pack()
    geoEqStrtLineButton.pack()
    geoEqPlaneButton.pack()
    geoEqCircleButton.pack()
    geoEqSphereButton.pack()
    geoEqEllipseButton.pack()
    doneGeoButton.pack_forget()

def ifDoneTrigButtonClick():
    trig1Button.pack_forget()
    trig2Button.pack_forget()
    trig3Button.pack_forget()
    trig1imgpic.pack_forget()
    trig2imgpic.pack_forget()
    trig3imgpic.pack_forget()
    trig1Button.pack()
    trig2Button.pack()
    trig3Button.pack()
    DoneTrigButton.pack_forget()
    

doneVolButton = tk.Button(text = 'Done', height = 4, width = 30, command = ifDoneVolButtonClick)
doneGeoButton = tk.Button(text = 'Done', height = 4, width = 30, command = ifDoneGeoButtonClick)
DoneTrigButton = tk.Button(text = 'Done', height = 4, width = 30, command = ifDoneTrigButtonClick)

def ifVolSphereClick():
    SphereFormula.pack()
    volSpherePic.pack()
    volRPrism.pack_forget()
    volPrism.pack_forget()
    volPyrandCone.pack_forget()
    volSphere.pack_forget()
    volCyl.pack_forget()
    volCube.pack_forget()
    menuEntry.pack_forget()
    doneVolButton.pack()
def ifVolPyrandConeClick():
    PyrandConeFormula.pack()
    volPyrandConePic.pack()
    volRPrism.pack_forget()
    volPrism.pack_forget()
    volPyrandCone.pack_forget()
    volSphere.pack_forget()
    volCyl.pack_forget()
    volCube.pack_forget()
    menuEntry.pack_forget()
    doneVolButton.pack()
def ifVolPrismClick():
    PrismFormula.pack()
    volPrismPic.pack()
    volRPrism.pack_forget()
    volPrism.pack_forget()
    volPyrandCone.pack_forget()
    volSphere.pack_forget()
    volCyl.pack_forget()
    volCube.pack_forget()
    menuEntry.pack_forget()
    doneVolButton.pack()
def ifVolRPrismClick():
    RPrismFormula.pack()
    volRPrismPic.pack()
    volRPrism.pack_forget()
    volPrism.pack_forget()
    volPyrandCone.pack_forget()
    volSphere.pack_forget()
    volCyl.pack_forget()
    volCube.pack_forget()
    menuEntry.pack_forget()
    doneVolButton.pack()
def ifVolCubeClick():
    CubeFormula.pack()
    volCubePic.pack()
    volRPrism.pack_forget()
    volPrism.pack_forget()
    volPyrandCone.pack_forget()
    volSphere.pack_forget()
    volCyl.pack_forget()
    volCube.pack_forget()
    menuEntry.pack_forget()
    doneVolButton.pack()
def ifVolCylinderClick():
    CylinderFormula.pack()
    volCylinderPic.pack()
    volRPrism.pack_forget()
    volPrism.pack_forget()
    volPyrandCone.pack_forget()
    volSphere.pack_forget()
    volCyl.pack_forget()
    volCube.pack_forget()
    menuEntry.pack_forget()
    doneVolButton.pack()

def ifGeoEulerButtonClick():
    geoEulerImgPic.pack()
    menuEntry.pack_forget()
    geoEulerButton.pack_forget()
    geoSumIntAngButton.pack_forget()
    geoPyTheoremButton.pack_forget()
    geoDistTwoPtButton.pack_forget()
    geoMidPtButton.pack_forget()
    geoEqStrtLineButton.pack_forget()
    geoEqPlaneButton.pack_forget()
    geoEqCircleButton.pack_forget()
    geoEqSphereButton.pack_forget()
    geoEqEllipseButton.pack_forget()
    doneGeoButton.pack()

def ifGeoSumIntAngButtonClick():
    geoSumIntAngImgPic.pack()
    menuEntry.pack_forget()
    geoEulerButton.pack_forget()
    geoSumIntAngButton.pack_forget()
    geoPyTheoremButton.pack_forget()
    geoDistTwoPtButton.pack_forget()
    geoMidPtButton.pack_forget()
    geoEqStrtLineButton.pack_forget()
    geoEqPlaneButton.pack_forget()
    geoEqCircleButton.pack_forget()
    geoEqSphereButton.pack_forget()
    geoEqEllipseButton.pack_forget()
    doneGeoButton.pack()

def ifGeoPyTheoremButtonClick():
    geoPyTheoremImgPic.pack()
    menuEntry.pack_forget()
    geoEulerButton.pack_forget()
    geoSumIntAngButton.pack_forget()
    geoPyTheoremButton.pack_forget()
    geoDistTwoPtButton.pack_forget()
    geoMidPtButton.pack_forget()
    geoEqStrtLineButton.pack_forget()
    geoEqPlaneButton.pack_forget()
    geoEqCircleButton.pack_forget()
    geoEqSphereButton.pack_forget()
    geoEqEllipseButton.pack_forget()
    doneGeoButton.pack()
def ifGeoDistTwoPtButtonClick():
    geoDistTwoPtsImgPic.pack()
    menuEntry.pack_forget()
    geoEulerButton.pack_forget()
    geoSumIntAngButton.pack_forget()
    geoPyTheoremButton.pack_forget()
    geoDistTwoPtButton.pack_forget()
    geoMidPtButton.pack_forget()
    geoEqStrtLineButton.pack_forget()
    geoEqPlaneButton.pack_forget()
    geoEqCircleButton.pack_forget()
    geoEqSphereButton.pack_forget()
    geoEqEllipseButton.pack_forget()
    doneGeoButton.pack()
def ifGeoMidPtButtonClick():
    geoMidpointsImgPic.pack()
    menuEntry.pack_forget()
    geoEulerButton.pack_forget()
    geoSumIntAngButton.pack_forget()
    geoPyTheoremButton.pack_forget()
    geoDistTwoPtButton.pack_forget()
    geoMidPtButton.pack_forget()
    geoEqStrtLineButton.pack_forget()
    geoEqPlaneButton.pack_forget()
    geoEqCircleButton.pack_forget()
    geoEqSphereButton.pack_forget()
    geoEqEllipseButton.pack_forget()
    doneGeoButton.pack()
def ifGeoEqStrtLineClick():
    geoEqStrtLineImgPic.pack()
    menuEntry.pack_forget()
    geoEulerButton.pack_forget()
    geoSumIntAngButton.pack_forget()
    geoPyTheoremButton.pack_forget()
    geoDistTwoPtButton.pack_forget()
    geoMidPtButton.pack_forget()
    geoEqStrtLineButton.pack_forget()
    geoEqPlaneButton.pack_forget()
    geoEqCircleButton.pack_forget()
    geoEqSphereButton.pack_forget()
    geoEqEllipseButton.pack_forget()
    doneGeoButton.pack()
def ifGeoEqCircleClick():
    geoEqCircleImgPic.pack()
    menuEntry.pack_forget()
    geoEulerButton.pack_forget()
    geoSumIntAngButton.pack_forget()
    geoPyTheoremButton.pack_forget()
    geoDistTwoPtButton.pack_forget()
    geoMidPtButton.pack_forget()
    geoEqStrtLineButton.pack_forget()
    geoEqPlaneButton.pack_forget()
    geoEqCircleButton.pack_forget()
    geoEqSphereButton.pack_forget()
    geoEqEllipseButton.pack_forget()
    doneGeoButton.pack()
def ifGeoEqPlaneClick():
    geoEqPlaneImgPic.pack()
    menuEntry.pack_forget()
    geoEulerButton.pack_forget()
    geoSumIntAngButton.pack_forget()
    geoPyTheoremButton.pack_forget()
    geoDistTwoPtButton.pack_forget()
    geoMidPtButton.pack_forget()
    geoEqStrtLineButton.pack_forget()
    geoEqPlaneButton.pack_forget()
    geoEqCircleButton.pack_forget()
    geoEqSphereButton.pack_forget()
    geoEqEllipseButton.pack_forget()
    doneGeoButton.pack()
def ifGeoEqSphereClick():
    geoEqSphereImgPic.pack()
    menuEntry.pack_forget()
    geoEulerButton.pack_forget()
    geoSumIntAngButton.pack_forget()
    geoPyTheoremButton.pack_forget()
    geoDistTwoPtButton.pack_forget()
    geoMidPtButton.pack_forget()
    geoEqStrtLineButton.pack_forget()
    geoEqPlaneButton.pack_forget()
    geoEqCircleButton.pack_forget()
    geoEqSphereButton.pack_forget()
    geoEqEllipseButton.pack_forget()
    doneGeoButton.pack()
def ifGeoEqEllipseClick():
    geoEqEllipseImgPic.pack()
    menuEntry.pack_forget()
    geoEulerButton.pack_forget()
    geoSumIntAngButton.pack_forget()
    geoPyTheoremButton.pack_forget()
    geoDistTwoPtButton.pack_forget()
    geoMidPtButton.pack_forget()
    geoEqStrtLineButton.pack_forget()
    geoEqPlaneButton.pack_forget()
    geoEqCircleButton.pack_forget()
    geoEqSphereButton.pack_forget()
    geoEqEllipseButton.pack_forget()
    doneGeoButton.pack()
def ifTrig1ButtonClick():
    trigButton.pack_forget()
    trig1Button.pack_forget()
    trig2Button.pack_forget()
    trig3Button.pack_forget()
    DoneTrigButton.pack()
    trig1imgpic.pack()
def ifTrig2ButtonClick():
    trigButton.pack_forget()
    trig1Button.pack_forget()
    trig2Button.pack_forget()
    trig3Button.pack_forget()
    DoneTrigButton.pack()
    trig2imgpic.pack()
def ifTrig3ButtonClick():
    trigButton.pack_forget()
    trig1Button.pack_forget()
    trig2Button.pack_forget()
    trig3Button.pack_forget()
    DoneTrigButton.pack()
    trig3imgpic.pack()

volSphere = tk.Button(text = 'The Volume of a Sphere', height = 4, width = 30, command = ifVolSphereClick)
volPyrandCone = tk.Button(text = "The Volume of a Pyramid/Cone", height = 4, width = 30, command = ifVolPyrandConeClick)
volPrism = tk.Button(text = "The Volume of a Prism", height = 4, width = 30, command = ifVolPrismClick)
volCube = tk.Button(text = "The Volume of a Cube", height = 4, width = 30, command = ifVolCubeClick)
volRPrism = tk.Button(text = "The Volume of a Parallelepipid/Cuboid", height = 4, width = 30, command = ifVolRPrismClick)
volCyl = tk.Button(text = 'The Volume of a Cylinder', height = 4, width = 30, command = ifVolCylinderClick)

geoEulerButton = tk.Button(text = 'Eulers Polyhedral Formula', height = 4, width = 30, command = ifGeoEulerButtonClick)
geoSumIntAngButton = tk.Button(text = 'Sum of interior angles of a polygon', height = 4, width = 30, command = ifGeoSumIntAngButtonClick)
geoPyTheoremButton = tk.Button(text = 'Pythagorean theorem', height = 4, width = 30, command = ifGeoPyTheoremButtonClick)
geoDistTwoPtButton = tk.Button(text = 'Distance between two points', height = 4, width = 30, command = ifGeoDistTwoPtButtonClick)
geoMidPtButton = tk.Button(text = 'Midpoints', height = 4, width = 30, command = ifGeoMidPtButtonClick)
geoEqStrtLineButton = tk.Button(text = 'Equation of a Straight Line', height = 4, width = 30, command = ifGeoEqStrtLineClick)
geoEqPlaneButton = tk.Button(text = 'Equation of a Plane', height = 4, width = 30, command = ifGeoEqPlaneClick)
geoEqCircleButton = tk.Button(text = 'Equation of a Circle', height = 4, width = 30, command = ifGeoEqCircleClick)
geoEqSphereButton = tk.Button(text = 'Equation of a Sphere', height = 4, width = 30, command = ifGeoEqSphereClick)
geoEqEllipseButton = tk.Button(text = 'Equation of an Ellipse', height = 4, width = 30, command = ifGeoEqEllipseClick)
trig1Button = tk.Button(text = 'Trigonometry Part 1', height = 4, width = 30, command = ifTrig1ButtonClick)
trig2Button = tk.Button(text = 'Trigonometry Part 2', height = 4, width = 30, command = ifTrig2ButtonClick)
trig3Button = tk.Button(text = 'Trigonometry Part 3', height = 4, width = 30, command = ifTrig3ButtonClick)
def ifMenuClick():
    volumeButton.pack_forget()
    geoButton.pack_forget()
    funcandEqButton.pack_forget()
    areaButton.pack_forget()
    netButton.pack_forget()
    volCube.pack_forget()
    volRPrism.pack_forget()
    volPrism.pack_forget()
    volPyrandCone.pack_forget()
    volSphere.pack_forget()
    volCyl.pack_forget()
    geoEulerButton.pack_forget()
    geoSumIntAngButton.pack_forget()
    geoPyTheoremButton.pack_forget()
    geoDistTwoPtButton.pack_forget()
    geoMidPtButton.pack_forget()
    geoEqStrtLineButton.pack_forget()
    geoEqPlaneButton.pack_forget()
    geoEqCircleButton.pack_forget()
    geoEqSphereButton.pack_forget()
    geoEqEllipseButton.pack_forget()
    funcandEqImgPic.pack_forget()
    trig1Button.pack_forget()
    trig2Button.pack_forget()
    trig3Button.pack_forget()
    trig1imgpic.pack_forget()
    trig2imgpic.pack_forget()
    trig3imgpic.pack_forget()
    volumeButton.pack()
    geoButton.pack()
    funcandEqButton.pack()
    areaButton.pack()
    netButton.pack()
    trigButton.pack()

def ifStartClick():
    volumeButton.pack()
    geoButton.pack()
    funcandEqButton.pack()
    areaButton.pack()
    netButton.pack()
    trigButton.pack()
    startButton.pack_forget()

def ifVolumeClick():
    volumeButton.pack_forget()
    geoButton.pack_forget()
    funcandEqButton.pack_forget()
    areaButton.pack_forget()
    netButton.pack_forget()
    trigButton.pack_forget()
    volCube.pack()
    volRPrism.pack()
    volPrism.pack()
    volPyrandCone.pack()
    volSphere.pack()
    volCyl.pack()

def ifGeoClick():
    volumeButton.pack_forget()
    geoButton.pack_forget()
    funcandEqButton.pack_forget()
    areaButton.pack_forget()
    netButton.pack_forget()
    trigButton.pack_forget()
    geoEulerButton.pack()
    geoSumIntAngButton.pack()
    geoPyTheoremButton.pack()
    geoDistTwoPtButton.pack()
    geoMidPtButton.pack()
    geoEqStrtLineButton.pack()
    geoEqPlaneButton.pack()
    geoEqCircleButton.pack()
    geoEqSphereButton.pack()
    geoEqEllipseButton.pack()
def ifFuncandEqClick():  
    volumeButton.pack_forget()
    geoButton.pack_forget()
    funcandEqButton.pack_forget()
    areaButton.pack_forget()
    netButton.pack_forget()
    trigButton.pack_forget()
    funcandEqImgPic.pack()
def ifAreaClick():
    volumeButton.pack_forget()
    geoButton.pack_forget()
    funcandEqButton.pack_forget()
    areaButton.pack_forget()
    netButton.pack_forget()
    trigButton.pack_forget()
def ifNetClick():
    volumeButton.pack_forget()
    geoButton.pack_forget()
    funcandEqButton.pack_forget()
    areaButton.pack_forget()
    netButton.pack_forget()
    trigButton.pack_forget()

def ifTrigClick():
    volumeButton.pack_forget()
    geoButton.pack_forget()
    funcandEqButton.pack_forget()
    areaButton.pack_forget()
    netButton.pack_forget()
    trigButton.pack_forget()
    trig1Button.pack()
    trig2Button.pack()
    trig3Button.pack()
    
workingOutBox1 = tk.Entry()

def ifWorkingOutClick():
    workingOutBox1.pack()
    clearWorkings.pack()

def ifclearWorkingsClick():
    workingOutBox1.pack_forget()
    clearWorkings.pack_forget()

clearWorkings = tk.Button(text = 'Clear', command = ifclearWorkingsClick)

volumeButton = tk.Button(text = "Volume", height = 4, width = 30, command = ifVolumeClick)
geoButton = tk.Button(text = "Geometry", height = 4, width = 30, command = ifGeoClick)
funcandEqButton = tk.Button(text = "Functions and Equations", height = 4, width = 30, command = ifFuncandEqClick)
areaButton = tk.Button(text = "Area", height = 4, width = 30, command = ifAreaClick)
netButton = tk.Button(text = "Nets", height = 4, width = 30, command = ifNetClick)
trigButton = tk.Button(text = "Trigonometry", height = 4, width = 30, command = ifTrigClick)

menuEntry = tk.Button(text = "Menu", height = 4, width = 30, command = ifMenuClick)
menuEntry.pack()

startButton = tk.Button(text = "Start", height = 4, width = 30, command = ifStartClick)
startButton.pack()

workingOut = tk.Button(text = 'Working Out', height = 4, width = 30, command = ifWorkingOutClick)
workingOut.pack()

parent.mainloop()






