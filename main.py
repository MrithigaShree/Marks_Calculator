from tkinter import *

root = Tk()
# Entries of subject 1
sub1 = Entry(root, width=15, borderwidth=5)
max1 = Entry(root, width=15, borderwidth=5)
# grid
sub1.grid(row=0, column=0)
max1.grid(row=0, column=2)
# insert statements
max1.insert(END, '100')
sub1.insert(END, '0')

# for error message
error_m = Label(root)


def error_message(a):
    global error_m
    error_m.destroy()
    if a == 0:
        error_m = Label(root, text='*Fill all values', fg='red')
        error_m.grid(row=1, column=2)


def avg():
    try:
        x = int(sub1.get())
        y = int(max1.get())
        z = (x / y) * 100
        avg_mark = Label(root, text='{:.2f}%'.format(z))
        avg_mark.grid(row=1, column=1)
        error_message(1)
    except ValueError:
        error_message(0)


# subject 1
sub1Button = Label(root, text='Marks attained', bg='black', fg='white')
sub1Button.grid(row=0, column=1)
max_sub1Button = Label(root, text='Max Marks', bg='black', fg='white')
max_sub1Button.grid(row=0, column=3)

# average button
average = Button(root, text='Percentage', bg='black', fg='white', command=avg)
average.grid(row=1, column=0)

root.mainloop()
