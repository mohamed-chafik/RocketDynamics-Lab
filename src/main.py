import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
frame = ctk.CTkFrame(
        master=app,
        width=200,
        height=400,
        border_color="#000000",   # Border color
        border_width=2,           # Border width
        corner_radius=10
        )
frame.grid(row=0,column=0)
app.mainloop()

