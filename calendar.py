#importing tkinter
from tkinter import *
#importing calendar module
import calendar
root=Tk()
root.title("Calendar")
year = 2020
myCal=calendar.calendar(year)
cal_year = Label(root,text=myCal,font = "Consolas 10 bold")
cal_year.pack()
root.mainloop()
