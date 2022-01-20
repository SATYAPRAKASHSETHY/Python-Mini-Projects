from tkinter import * #Label, Tk
import time
clock_window = Tk()
clock_window.title("My Digital Clock")
clock_window.geometry("420x150")
clock_window.resizable(1,1)

text_font = ("Boulder", 68, "bold")
background =  "#f2e760"#b
foreground = "#363529"
borderwidth = 130
label = Label(clock_window, font = text_font,bg = background, fg = foreground, bd = borderwidth)
label.grid(row =0, column = 1)

def digital_clock():
	time_live= time.strftime("%H: %M: %S")
	label.config(text = time_live)
	label.after(200,digital_clock)

digital_clock()

clock_window.mainloop()
