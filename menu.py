from tkinter import *
from customtkinter import *

from app import *

set_default_color_theme("green")

root = CTk()
root.config(padx=160, pady=90)
root.title("Weather viewer")
root.iconbitmap("D:\programmation\Github\API_voile\icon.ico")

def results(city, days)->None:
    print(days)
    resultWindow = CTkToplevel(root)
    resultWindow.after(250, lambda: resultWindow.iconbitmap("D:\programmation\Github\API_voile\icon.ico"))
    resultWindow.title(f"Informations in {city}")
    results = get_weather("77eb92f97e104bf6b9773753242709", city, days)
    
    # teste si il y a une erreur
    if type(results)!=str:
        row_date = 0
        column_date = 0
        day_tabs: list[LabelFrame] = []
        time_tabs: list[LabelFrame] = []
        wind_mls_labels: list[CTkLabel] = []
        wind_dir_labels: list[CTkLabel] = []
        
        for value in results:
            row_time = 1
            column_time = 0
            
            if row_date == 5:
                column_date += 1
                row_date = 0
                
            if value["values"]!=[]:
                day_tab = CTkFrame(master=resultWindow, width=160, height=90)
                text = CTkLabel(master=day_tab, text=f"{value["date"]}", font=(font, title_size))
                day_tabs.append((day_tab, text))
                day_tab.grid(row=row_date, column=column_date, sticky="nsew", padx=2, pady=2)
                text.grid(row=0, column=0, columnspan=1, rowspan=1, sticky="new")
                
                for param in value["values"]:
                    if row_time == 3:
                        column_time += 1
                        row_time = 0
                    
                    time_tab = CTkFrame(master=day_tab, width=80, height=45)
                    time_text = CTkLabel(master=time_tab, text=f"{param["time"]}", font=(font, title_size))
                    time_tabs.append((time_tab, time_text))
                    time_tab.grid(row=row_time, column=column_time, padx=2, pady=2)
                    time_text.grid(row=0, column=0, columnspan=2)
                    
                    wind_mls_label = CTkLabel(master=time_tab, text=f"force: {param["wind_mls"]} miles", font=(font, size))
                    wind_mls_labels.append(wind_mls_label)
                    wind_mls_label.grid(row=1, column=0, sticky="ew")
                    
                    wind_dir_label = CTkLabel(master=time_tab, text=f"direction: {param["wind_dir"]}", font=(font, size))
                    wind_dir_labels.append(wind_dir_label)
                    wind_dir_label.grid(row=2, column=0, sticky="ew")
                    
                    row_time += 1
                    
                row_date += 1
    else:
        text = CTkLabel(resultWindow, text=results, font=(font, size))
        text.pack(side="top")
            
    resultWindow.pack_propagate()


city = StringVar()
days = IntVar()
city_UI = CTkLabel(master=root, text="wanted city", anchor="n", font=(font, title_size))
city_Var = CTkEntry(master=root, textvariable=city, font=(font, size))
future_day = CTkSlider(master=root, from_=1, to=5, number_of_steps=4, width=20, height=100, orientation=VERTICAL)

run_Button = CTkButton(master=root, text="locate", command=lambda :results(city.get(), int(future_day.get())), font=(font, size))

future_day.grid(row=0, column=0, rowspan=3, columnspan=2, sticky="nsw")
city_UI.grid(row=0, column=3, sticky="n")
city_UI.grid_anchor(anchor="n")
city_Var.grid(row=1, column=3 ,sticky="nsew")
run_Button.grid(row=2, column=3, sticky="nsew")

root.mainloop()