from tkinter import *
from PIL import Image
from io import BytesIO

from app import *

root = Tk()
root.config(padx=160, pady=90)
root.title("Weather viewer")
root.iconbitmap("icon.ico")

def results(city)->None:
    resultWindow = Toplevel(root)
    results = get_weather("77eb92f97e104bf6b9773753242709", city)
    
    location_UI = Label(resultWindow, text=f"Location: {results["location"]}")
    
    resultWindow.pack_propagate()
    

city = StringVar()
city_UI = Label(root, text="wanted city", anchor="center")
city_Var = Entry(root, textvariable=city)

run_Button = Button(root, text="locate", command=lambda :results(city.get()))

city_UI.grid(row=0, column=0)
city_Var.grid(row=0, column=1)
run_Button.grid(row=1, column=0)

root.mainloop()