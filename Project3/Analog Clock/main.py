#analog clock

import tkinter as ui
import time
import math
 
def update_clock():
    hr=int(time.strftime("%I"))
    min=int(time.strftime("%M"))
    sec=int(time.strftime("%S"))

    sec_x= sec_hand_len * math.sin(math.radians(sec*6)) + center_x
    sec_y= -1*sec_hand_len * math.cos(math.radians(sec*6)) + center_y
    canvas.coords(sec_hand,center_x,center_y,sec_x,sec_y)
    window.after(1000,update_clock)

    min_x= min_hand_len * math.sin(math.radians(min*6)) + center_x
    min_y= -1*min_hand_len * math.cos(math.radians(min*6)) + center_y
    canvas.coords(min_hand,center_x,center_y,min_x,min_y)
    window.after(1000,update_clock)

    hr_x= hr_hand_len * math.sin(math.radians(hr*30)) + center_x
    hr_y= -1*hr_hand_len * math.cos(math.radians(hr*30)) + center_y
    canvas.coords(hr_hand,center_x,center_y,hr_x,hr_y)
    window.after(1000,update_clock)


window = ui.Tk()
window.geometry('400x400')

canvas= ui.Canvas(window, width=400, height=400,bg='red')
canvas.pack(expand=True, fill='both')

#creat bg
bg=ui.PhotoImage(file='clock.png')
canvas.create_image(200,200,image=bg)

#creat clock hands
center_x=200
center_y=200
hr_hand_len=60
min_hand_len=80
sec_hand_len=95

#drawing clock hands
sec_hand=canvas.create_line(200,200,200+sec_hand_len,200+sec_hand_len,width=1.5,fill='purple')
min_hand=canvas.create_line(200,200,200+min_hand_len,200+min_hand_len,width=2,fill='white')
hr_hand=canvas.create_line(200,200,200+hr_hand_len,200+hr_hand_len,width=4,fill='white')
update_clock()

window.mainloop()
