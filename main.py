from tkinter import *

root = Tk()
root.title('Marks Calculator')
error_m = Label(root)


def error_message(a):
    global error_m
    error_m.destroy()
    word = '*Fill all Values'
    if a in [0, 5]:
        if a == 5:
            word = 'Max marks can\'t be 0'

        error_m = Label(root, text=word, fg='red')
        error_m.grid(row=tot_sub, column=4)


avg_label = Label(root)
tot_avg_label = Label(root)


def show(*args):
    global avg_label, tot_avg_label
    avg_label.destroy()
    tot_avg_label.destroy()
    tot_avg = 0

    for i in range(tot_sub):  # Loop through the number of subjects
        attained = attained_marks[i].get()  # Get the indexed item from the list and use get()
        max_mark = max_marks[i].get()
        try:
            avg = (int(attained) / int(max_mark)) * 100
            tot_avg += avg
            word, color = 'Percentage : {:.2f}%'.format(avg), 'green'
            if avg > 101:
                word = 'Wrong Values'
                color = 'red'
            avg_label = Label(root, text=word, fg=color)
            avg_label.grid(row=i, column=4)
            error_message(1)
        except ValueError:
            error_message(0)
        except ZeroDivisionError:
            error_message(5)

    tot_avg = tot_avg / tot_sub
    tot_avg_label = Label(root, text='Total Percentage : {:.2f} %'.format(tot_avg))
    tot_avg_label.grid(row=tot_sub, column=2)
    # Print the values out


attained_marks = []  # Empty list to populate later
max_marks = []  # Empty list to populate later
tot_sub = int(input('Enter no. of subjects: '))  # Number of subjects
for i in range(tot_sub):
    sub1 = Entry(root, width=15, borderwidth=5)
    sub1.grid(row=i, column=0)
    attained_marks.append(sub1)  # Append each entry to the list

    max1 = Entry(root, width=15, borderwidth=5)
    max1.grid(row=i, column=2)
    max_marks.append(max1)  # Append each entry to the list

    sub1label = Label(root, text='Marks attained', bg='grey', fg='white')
    sub1label.grid(row=i, column=1, padx=5)

    max_sub1label = Label(root, text='Max Marks', bg='grey', fg='white')
    max_sub1label.grid(row=i, column=3, padx=5)

avgButton = Button(root, text='Average', bg='green', fg='black', command=root.bind('<Return>', show))
avgButton.grid(row=tot_sub, column=1)

root.mainloop()
