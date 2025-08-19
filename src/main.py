import customtkinter as ctk
from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()

# Configure main grid - 1 row, 2 columns
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=0)  # Fixed width for data frame
app.grid_columnconfigure(1, weight=1)  # Expanding width for squares

# Data Frame - Left side (full height, fixed width)
data_frame = ctk.CTkFrame(
    master=app, 
    width=300,  # Fixed width
    fg_color="#2c3e50", 
    corner_radius=10
)
data_frame.grid(row=0, column=0, sticky="ns", padx=(10, 5), pady=10)

# Make data frame take full height
data_frame.grid_propagate(False)  # Prevents frame from shrinking to fit content

Altitude_entry = ctk.CTkEntry(data_frame, placeholder_text="CTkEntry")
Altitude_entry.pack(padx=20)





# Fill remaining space at bottom
ctk.CTkLabel(data_frame, text="", text_color="white").pack(expand=True)

# Squares Container - Right side (fills remaining width and full height)
squares_container = ctk.CTkFrame(master=app, fg_color="transparent")
squares_container.grid(row=0, column=1, sticky="nsew", padx=(5, 10), pady=10)

# Configure grid inside squares container (3 columns)
squares_container.grid_rowconfigure(0, weight=1)
squares_container.grid_rowconfigure(1, weight=1)
squares_container.grid_rowconfigure(2, weight=1)
squares_container.grid_columnconfigure(0, weight=1)
squares_container.grid_columnconfigure(1, weight=1)
squares_container.grid_columnconfigure(2, weight=1)

# Create 9 square frames (3 rows × 3 columns)
square_frames = []
colors = ["#e74c3c", "#3498db", "#2ecc71", "#f39c12", "#9b59b6", "#1abc9c", 
          "#e67e22", "#34495e", "#d35400"]

for row in range(3):
    for col in range(3):
        index = row * 3 + col
        square = ctk.CTkFrame(
            master=squares_container,
            fg_color=colors[index],
            corner_radius=15,
            border_width=2,
            border_color="white"
        )
        square.grid(
            row=row, 
            column=col, 
            padx=10, 
            pady=10, 
            sticky="nsew"  # Make squares expand to fill their grid cells
        )
        
        # Add label to each square
        label = ctk.CTkLabel(
            square, 
            text=f"Square {index+1}", 
            text_color="white",
            font=("Arial", 14, "bold")
        )
        label.place(relx=0.5, rely=0.5, anchor="center")
        
        square_frames.append(square)
app.mainloop()

