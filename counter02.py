import tkinter as tk


class Counter(tk.Frame):
    def __init__(self, master=None, value=0):
        self.value = value


        tk.Frame.__init__(self, master)
        font = ('Helevetica', 32, 'bold')
        self.label = tk.Label(self, text=self.getText(), font=font, bg='red')
        self.button = tk.Button(self, text='Click', command=self.clicked)
        self.label.pack()
        self.button.pack()

    def clicked(self):
        self.value += 1
        self.label.configure(text=self.getText())

    def getText(self):
        return 'Count:{}'.format(self.value)


f = tk.Frame()
c1 = Counter(value=0, master=f)
c2 = Counter(value=5, master=f)
c1.pack()
c2.pack()
f.pack()
f.mainloop()
