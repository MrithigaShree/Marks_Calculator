from tkinter import *


root = Tk()
x, y, d = 0, 0, {}
for i in range(1, int(input('Enter no of subjects')) + 1):
    sub1 = Entry(root, width=15, borderwidth=5)
    sub1.grid(row=x, column=y)
    max1 = Entry(root, width=15, borderwidth=5)
    max1.grid(row=x, column=y+2)
    sub1label = Label(root, text='Marks attained', bg='black', fg='white')
    sub1label.grid(row=x, column=y+1)
    max_sub1label = Label(root, text='Max Marks', bg='black', fg='white')
    max_sub1label.grid(row=x, column=y+3)
    x += 1


root.mainloop()
