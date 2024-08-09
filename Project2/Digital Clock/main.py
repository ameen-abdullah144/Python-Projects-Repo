#Digital Clock

import tkinter as ui
import time
 
def update_clock():
    hours=time.strftime("%I")
    min=time.strftime("%M")
    sec=time.strftime("%S")
    am_pm=time.strftime("%p").lower()
    update=hours    + ":" + min + ":" + sec +" "+am_pm
    digital_clocl_lable.config(text=update)
    digital_clocl_lable.after(1000, update_clock)

window = ui.Tk()
digital_clocl_lable=ui.Label(window,text="00:00:00",font='Helvetica 72 bold') 
digital_clocl_lable.pack()

update_clock()

window.mainloop()
