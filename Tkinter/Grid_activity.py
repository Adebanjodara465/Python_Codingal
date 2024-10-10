import tkinter as tk #the tk is just a nickname

window = tk.Tk()

for i in range(4):
    for j in range(4):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=3
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\ncolumn {j}")
        label.pack()
        
window.mainloop()