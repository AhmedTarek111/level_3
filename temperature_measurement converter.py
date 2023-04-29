#First way#
#================================================================================================================
#1--------------------------------------------------------------------------------------------------------------
def  convert_Fahrenheit_to_Celcius(Fahrenheit):
    return f"Celcius = {((Fahrenheit-32)*5)/9}"  

def convert_Celcius_Fahrenheit(Celcius):
    return f"Fahrenheit = {(Celcius * 1.8)+32}"
#---------------------------------------------------------------------------------------------------------------

def convert_inches_to_centimeter(inches):
    return f"cm = {inches*2.54}"
print(convert_inches_to_centimeter(10))

def convert_centimeters_to_inches(centimeters):
    return f"centimeters = {centimeters/2.54}"
print(convert_centimeters_to_inches(25.4))

##second way##
#================================================================================================================
#-----------------------------------------------lambda----------------------------------------------------
Fahrenheit_to_Celcius=lambda Fahrenheit:f"Celcius = {((Fahrenheit-32)*5)/9}"  
Celcius_Fahrenheit= lambda Celcius:f"Fahrenheit = {(Celcius * 1.8)+32}"
#-----------------------------------------------lambda----------------------------------------------------
inches_to_centimeter=lambda inches:f"cm = {inches*2.54}"
centimeters_to_inches=lambda centimeters:f"centimeters = {centimeters/2.54}"
#---------------------------------------------------------------------------------------------------------

###third way###
#================================================================================================================
class Temperture_converter:
    def __init__(self,Celcius=0,Fahrenheit=0,centimeters=0,inches=0):
           self.Celcius=Celcius
           self.Fahrenheit=Fahrenheit
           self.centimeters=centimeters
           self.inches=inches
           print(''' 
            Welcome to Temperature converter
            ---------------------------------------------
            F= Fahrenheit    C= Celsius   I= inches
            ---------------------------------------------
            1- F -> C
            2- C -> F
            3- I -> Cm
            4- cm -> I
            5- Exit
            ''')

           User_choice = float(input("Please enter the number of process = "))
           if User_choice == 1:
                Fahrenheit = float(input("Fahrenheit = "))
                print(self.convert_Fahrenheit_to_Celcius(Fahrenheit))
           elif User_choice == 2:
                Celsius = float(input("Celsius = "))
                print(self.convert_Celcius_Fahrenheit(Celsius))
           elif User_choice == 3:
                inches = float(input("Inches = "))
                print(self.convert_inches_to_centimeter(inches))
           elif User_choice == 4:
                centimeters = float(input("Centimeters = "))
                print(self.convert_centimeters_to_inches(centimeters))
           elif User_choice == 5:
                 return
        
    convert_Fahrenheit_to_Celcius= lambda self,Fahrenheit:f"Celcius = {((Fahrenheit-32)*5)/9}" 

    convert_Celcius_Fahrenheit=lambda self,Celcius: f"Fahrenheit = {(Celcius * 1.8)+32}"

    convert_inches_to_centimeter=lambda self,inches:f"cm = {inches*2.54}"
#================================================================================================================