import tkinter as tk


window = tk.Tk()
window.title("Password generator")
window.geometry("400x300")
window.mainloop()
mylabel = tk.Label(text="ABCD ")
mylabel.grid(column=0, row=0)
window.mainloop()
button_name = tk.Button(window, text = "some text")
button_name.grid(column=1,row=0)