import tkinter as tk


class Counter:
    def __init__(self, value):
        self.value = value
        frame = tk.Frame()
        font = ('Helevetica', 32, 'bold')
        self.label = tk.Label(frame, text=self.getText(), font=font, bg='red')
        button = tk.Button(frame, text='Click', command=self.clicked)
        self.label.pack()
        button.pack()
        frame.pack()
        frame.mainloop()


    def clicked(self):
        self.value += 1
        self.label.configure(text=self.getText())

    def getText(self):
        return 'Count:{}'.format(self.value)


c = Counter(0)