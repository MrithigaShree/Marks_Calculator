from tkinter import *

root = Tk()
root.title('Marks Calculator')
error_m = Label(root)


def error_message(a, tot_sub):
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
attained_marks = []
max_marks = []


def rows_and_columns(*args):
    global attained_marks, max_marks
    sub_button.destroy()
    # Empty list to populate later
    tot_sub = int(sub.get())  # Number of subjects
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
    show()


def show(*args):
    global avg_label, tot_avg_label
    avg_label.destroy()
    tot_avg_label.destroy()
    tot_avg = 0
    tot_sub = int(sub.get())

    for i in range(tot_sub):  # Loop through the number of subjects
        if len(attained_marks) > 1:
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
                error_message(1, tot_sub)
            except ValueError:
                error_message(0, tot_sub)
            except ZeroDivisionError:
                error_message(5, tot_sub)

    tot_avg = tot_avg / tot_sub
    tot_avg_label = Label(root, text='Total Percentage : {:.2f} %'.format(tot_avg), fg='green')
    tot_avg_label.grid(row=tot_sub, column=2)
    avg_button = Button(root, text='Average', bg='green', fg='black', command=root.bind('<Return>', show))
    avg_button.grid(row=tot_sub, column=1)
    # Print the values out


sub = Entry(root, width=15)
sub.grid(row=0, column=0)
sub.insert(END, '0')
sub_button = Button(root, text='No of Subjects', command=rows_and_columns, bg='green')
sub_button.grid(row=0, column=1)

root.mainloop()
