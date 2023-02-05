import tkinter as tk
from tkinter import messagebox
import cv2

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")

        self.menubar = tk.Menu(self.root)
        
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.onclosing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close without question", command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.show_message)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text='t = ', font=('Arial', 18))
        self.label.pack()
        self.label.place(x=10, y=10)

        self.textbox = tk.Text(self.root, height=1, width=20, font=('Arial', 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack()
        self.textbox.place(x=50, y=10)

        self.check_state = tk.IntVar()

        self.plot_button = tk.Button(self.root, command = self.plot, height=1, width = 12, text = "Plot f(x) = x**t", font=('Arial', 16))
        self.plot_button.pack()
        self.plot_button.place(x=300, y=10)

        self.plotlabel = tk.Label(self.root, height=10, width=10)
        self.plotlabel.pack()
        self.plotlabel.place(x=10, y=40, relheight=0.5, relwidth=0.9)
        self.plotlabel.config(bg= "gray")

        self.root.mainloop()
    

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))
    

    def shortcut(self, event):
        if event.state == 12 and event.keysym == 'Return':
            self.show_message()


    def onclosing(self):
        if messagebox.askyesno(title="Quit?", message='Want to quit?'):
            self.root.destroy()
    

    def plot(self):
        img = cv2.imread("image.png")

MyGUI()