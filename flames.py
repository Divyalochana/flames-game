import tkinter
from tkinter import *
from tkinter import messagebox

window = tkinter.Tk()
window.geometry('500x350')
window.title("FLAMES")
window.name1 = StringVar()
window.name2 = StringVar()

#UI Design
name_1 = Label(window, text="enter 1st name :", font=("times new roman", 15, "bold")).grid(row=0, column=0)
entry_1 = Entry(window, bd=4, font=("", 15, "bold"), textvariable=window.name1).grid(row=0, column=1, padx=30, pady=40)

name_2 = Label(window, text="enter another name :", font=("times new roman", 15, "bold")).grid(row=1, column=0)
entry_2 = Entry(window, bd=4, font=("", 15, "bold"), textvariable=window.name2).grid(row=1, column=1, padx=30, pady=40)


def rem_match_char(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]

                list1.remove(c)
                list2.remove(c)

                list3 = list1 + ["*"] + list2
                return [list3, True]
    list3 = list1 + ["*"] + list2
    return [list3, False]


def ret_flames():
    name1 = window.name1.get()
    name1 = name1.lower()
    name1_list = list(name1)

    name2 = window.name2.get()
    name2 = name2.lower()
    name2_list = list(name2)

    proceed = True
    while proceed:
        ret_list = rem_match_char(name1_list, name2_list)
        con_list = ret_list[0]
        proceed = ret_list[1]

        star_index = con_list.index("*")

        person1 = con_list[: star_index]
        person2 = con_list[star_index + 1:]

    count = len(person1) + len(person2)
    res = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]

    while len(res) > 1:
        split_index = (count % len(res) - 1)
        if split_index >= 0:
            right = res[split_index + 1:]
            left = res[:split_index]
            res = right + left
        else:
            res = res[: len(res) - 1]

    messagebox.showinfo("completed", res)


but = Button(window, text="Find", fg="black", bg="grey", font=("times new roman", 17, "bold"),
             command=ret_flames).grid(
    row=2, columnspan=2)

window.mainloop()
