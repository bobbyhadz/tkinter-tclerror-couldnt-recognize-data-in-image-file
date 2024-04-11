# \_tkinter.TclError: couldn't recognize data in image file


from tkinter import *

root = Tk()

canv = Canvas(root, width=500, height=500, bg='white')
canv.grid(row=2, column=3)

# ✅ Changed the image to .png
img = PhotoImage(file="house.png")

canv.create_image(0, 0, anchor=NW, image=img)

root.mainloop()