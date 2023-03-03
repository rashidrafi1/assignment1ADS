import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cmd = pd.read_csv("climat_1.csv")
print(cmd)

def bar(cmd,xlabel,ylabel,title):
 
   plt.figure()


   #plt.axes(["Year"])

   plt.bar(cmd["Year"],cmd["CO2"], label ="CO2" )
   plt.bar(cmd["Year"],cmd["CH4"], label ="CH4" )
   plt.xlabel("Year ")
   plt.ylabel("Gases (Cubic metres) Environment ")
   plt.title("Gases Quantity in climate")

   plt.legend()
   plt.show()       
    
bar(cmd,"Year ","Gases (Cubic metres) Environment ","Gases quantity in clima")

#line graph

cmd = pd.read_csv("climat_1.csv", )#index_col=0)
print(cmd)

def line(cmd,xlabel,ylabel,title):
 
    plt.figure()
    plt.plot(cmd["Year"],cmd["CO2"],label= "CO2")
    plt.plot(cmd["Year"],cmd["CH4"], label="CH4")
    plt.plot(cmd["Year"],cmd["N2O"], label="N2O")
    plt.plot(cmd["Year"],cmd["CFC-12"],label="CFC-12")
    plt.plot(cmd["Year"],cmd["CFC-11"],label="CFC-11")
    plt.plot(cmd["Year"],cmd["Aerosols"],label="Aerosols")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()
    
line(cmd,"Year ","Gases (Cubic metres) Environment ","Gases quantity in climate")

#pie graph

def generate_pie_chart(data, year):
    list=["CO2","CH4","N2O","CFC-11","CFC-12","Aerosols"]
    plt.figure()
    plt.pie(data, labels=list, autopct="%1.f%%")
    plt.title("Data in "+ str(year))
    plt.show()

# Example usage
#cmd = pd.DataFrame([[50, 20, 10, 5, 10, 5], [40, 30, 15, 5, 5, 5], [30, 30, 20, 10, 5, 5]], columns=["CO2","CH4","N2O","CFC-11","CFC-12","Aerosols"])
cmd = pd.read_csv("climat_1.csv", index_col=0)
print(cmd)
generate_pie_chart(cmd.iloc[0], 1983)
generate_pie_chart(cmd.iloc[2], 1985)













