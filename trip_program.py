from tkinter import *
from tkinter import ttk

def clear():
    choicebox.set("")
    itembox.selection_clear(0, END)
    notebox.delete(1.0, END)


def cbox(x):
    tvar.set(choicebox.get())


def save():
    try:
        file = open('travel_log.txt', 'a')
        cvar = (itembox.curselection())
        file.write("\n\nCountry: %s\nMethod of Travel: %s\nMonth: %s\nUser Notes: %s " % ((itembox.get(cvar, None)), tvar.get(), sp.get(), notebox.get(1.0, END)))
        clear()
    except:
        errmessage = Toplevel()
        errmessage.geometry('200x110')
        errmessage.title("Error")
        ermsg = Message(errmessage, text="You have an error in your selection. Please make sure you have selected everything needed.")
        ermsg.pack()
        close1 = Button(errmessage, text="Close", command=errmessage.destroy)
        close1.pack()


def exit():
    root.destroy()


def about():
    abt = Toplevel()
    abt.geometry('250x130')
    abt.title("About")
    abtmsg = Message(abt, text="This program is an example of a Travel log, used to input information about the user's trips around the world.")
    abtmsg.pack()
    close = Button(abt, text="Close", command=abt.destroy)
    close.pack()


root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)


mframe=Frame()
mframe.grid(column=0, row=1)


lframe=Frame()
lframe.grid(column=0, row=0)


label = Label(lframe, text="Travel Log\n----------")
label.grid(column=0, row=0)


slab=Label(mframe, text="Month:  ")
slab.grid(column=0, row=2, sticky='e')
spinval = StringVar()
sp = Spinbox(mframe,state='readonly', wrap=True, width=28, values=("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"))
sp.grid(column=1, row=2, sticky='w')


tvar = StringVar()
tlab=Label(mframe, text="Transportation:  ")
tlab.grid(column=0, row=0, sticky='e')
travel = ["Airplane", "Train", "Car", "Boat"]
choicebox = ttk.Combobox(mframe, width=27, state='readonly', value=travel)
choicebox.grid(column=1, row=0, sticky='w')
choicebox.bind('<<ComboboxSelected>>', cbox)


notebox = Text(mframe, width=20, height=10, wrap='word')
notebox.grid(column=4, row=1, sticky='w')


clab=Label(mframe, text="Countries:  ")
clab.grid(column=0, row=1, sticky='e')
countries = ["Argentina", "Australia", "The Bahamas", "Belgium", "Brazil", "Czech Republic", "France", "Germany", "Ireland", "Italy", "Russia", "Singapore", "Sweden", "United Kingdom", "United States", "Vietnam", "Other"]
itembox = Listbox(mframe, width=30, height=10, listvariable=countries, selectmode=SINGLE)
for item in countries:
    itembox.insert('end', '%s' % item)
itembox.grid(column=1, row=1, sticky='w')
itembox.bind('<FocusIn>')


l1 = Label(mframe, text="   Notes:  ")
l1.grid(column=3, row=1, sticky='e')
l2 = Label(mframe, text="")
l2.grid(row=3, column=1)
l3 = Label(mframe, text=" ")
l3.grid(row=3, column=5)


calculate = Button(mframe, text="SUBMIT", command=save, width=25)
calculate.grid(column=1, row=4)


clearb = Button(mframe, text="CLEAR", command=clear, width=10)
clearb.grid(column=3, row=4, sticky='w', columnspan=2)


s = ttk.Scrollbar(mframe, orient=VERTICAL, command=itembox.yview)
s.grid(column=2, row=1, sticky='nse')
itembox.configure(yscrollcommand=s.set)


root.mainloop()
