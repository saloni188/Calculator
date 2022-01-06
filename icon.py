from tkinter import *
from PIL import Image, ImageTk

app = Tk()
app.title("Images")
app.resizable(0, 0)
app["bg"]="#554f57"

frame=Frame(app, width=600, height=600, relief=GROOVE, bd=2)
frame.pack(padx=10, pady=10)
btn_font=("Calibri",11)
btn_bg="pink"
btn_fg="grey"

img1 = Image.open("C:\Calculator\d1.jfif")
img1.thumbnail((550, 450))
img2 = Image.open("C:\Calculator\d2.jfif")
img2.thumbnail((550, 450))
img3 = Image.open("C:\Calculator\d3.jfif")
img3.thumbnail((550, 450))
img4 = Image.open("C:\Calculator\d4.jfif")
img4.thumbnail((550, 450))

image1 = ImageTk.PhotoImage(img1)
image2 = ImageTk.PhotoImage(img2)
image3 = ImageTk.PhotoImage(img3)
image4 = ImageTk.PhotoImage(img4)
images = [image1, image2, image3, image4]

n = 0
image_label = Label(frame, image=images[n])
image_label.pack()

def previous():
    global n
    n = n - 1
    try:
        image_label.config(image=images[n])
    except:
        n = 0
        previous()
def next():
    global n
    n = n + 1
    try:
        image_label.config(image=images[n])
    except:
        n = -1
        next()

previous_btn = Button(app, text="Previous", bg=btn_bg, command=previous)
previous_btn.pack(side=LEFT, padx=60, pady=5)
exit_btn = Button(app, text="Exit", width=8, bg=btn_bg, command=app.destroy)
exit_btn.pack(side=LEFT, padx=60, pady=5)
next_btn = Button(app, text="Next", width=8, command=next)
next_btn.pack(side=LEFT, padx=60, pady=5)

app.mainloop()