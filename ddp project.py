import tkinter as tk
from tkinter import ttk
import time
from PIL import ImageTk, Image

root = tk.Tk()
root.title('Timer')
root.geometry('400x600')
root.config(bg='#000')
root.resizable(False, False)

# text time
heading = ttk.Label(root, text='Timer', font='arial 20 bold', background='#000', foreground='#ea3548')
heading.pack(pady=10)

# current time
label = ttk.Label(root, font='arial 15 bold', text='current time', background='papaya whip').place(x=65, y=70)

def clock():
    current_time_string = time.strftime('%H:%M:%S %p')
    current_time.config(text=current_time_string)
    current_time.after(1000, clock)

current_time = tk.Label(root, font='arial 15 bold', text='', fg='#000', bg='#fff')
current_time.place(x=190, y=70)
clock()

# timer
hrs = tk.StringVar()
entry = tk.Entry(root, textvariable=hrs, width=2, font='arial 50', background='#000', foreground='#fff', border=0).place(x=30, y=155)
hrs.set('00')

mins = tk.StringVar()
entry = tk.Entry(root, textvariable=mins, width=2, font='arial 50', background='#000', foreground='#fff', border=0).place(x=150, y=155)
mins.set('00')

sec = tk.StringVar()
entry = tk.Entry(root, textvariable=sec, width=2, font='arial 50', background='#000', foreground='#fff', border=0).place(x=270, y=155)
sec.set('00')

# text hours sec minus
label = tk.Label(root, text='hours', font='arial 12', bg='#000', fg='#fff').place(x=105, y=200)

label = tk.Label(root, text='min', font='arial 12', bg='#000', fg='#fff').place(x=225, y=200)

label = tk.Label(root, text='sec', font='arial 12', bg='#000', fg='#fff').place(x=345, y=200)

def Timer():
    times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())

    while times> -1:
        minute, second=(times//60, times %60)

        hour = 0
        if minute > 60:
            hour, minute=(minute//60,minute%60)

        sec.set(second)
        mins.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)

        times -= 1

def brush():
    hrs.set('00')
    mins.set('10')
    sec.set('00')
    Timer()

def face():
    hrs.set('00')
    mins.set('15')
    sec.set('00')
    Timer()

def eggs():
    hrs.set('00')
    mins.set('30')
    sec.set('00')
    Timer()

# button
button = tk.Button(root, text='start', background='#ea3548', bd=0, foreground='#fff', width=20, height=2, font='arial 10 bold')
button.pack(padx=5, pady=40, side='bottom')

# gambar
image_brush_path = 'image/brush.png'
image_brush_pil = Image.open(image_brush_path)
image_brush_tk = ImageTk.PhotoImage(image_brush_pil)

button_brush = tk.Button(root, image=image_brush_tk, background='#000', border=0, command=brush)
button_brush.place(x=7, y=280)

image_face_path= 'image/face.png'
image_face_pil = Image.open(image_face_path)
image_face_tk = ImageTk.PhotoImage(image_face_pil)

button_face= tk.Button(root, image=image_face_tk, background='#000', border=0, command=face)
button_face.place(x=137, y=280)

image_eggs_path= 'image/eggs.png'
image_eggs_pil = Image.open(image_eggs_path)
image_eggs_tk = ImageTk.PhotoImage(image_eggs_pil)

button_eggs = tk.Button(root, image=image_eggs_tk, background='#000', border=0, command=eggs)
button_eggs.place(x=267, y=280)


root.mainloop()