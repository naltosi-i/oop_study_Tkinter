import tkinter as tk


frame = tk.Frame()
font = ('Helevetica', 32, 'bold')
label1 = tk.Label(frame, text='Hello Tk', font=font, bg='red')
label2 = tk.Label(frame, text='Hello Python', font=font, bg='blue')
label1.pack(fill=tk.X)
label2.pack(fill=tk.X)
frame.pack()
frame.mainloop()
