import customtkinter as ctk
from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
def plot():
    fig = Figure(figsize=(3,3))
    y = [i**2 for i in range(101)]
    plot1 = fig.add_subplot(111)
    plot1.plot(y)
    canvas = FigureCanvasTkAgg(fig,master=app)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0,padx=10)


plot()
app.mainloop()

