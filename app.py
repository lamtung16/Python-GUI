import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import numpy as np

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x300")

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
        t = int(self.textbox.get("1.0", "end-1c"))

        x = np.arange(1.0, 20.0, 0.01)

        # export image
        plt.plot(x, np.power(x, t), 'k')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.savefig("image.pdf")
        plt.savefig("image.png")
        plt.close()

        img = ImageTk.PhotoImage(Image.open("image.png").resize([400, 200]))
        plotlabel = tk.Label(self.root, image=img)
        plotlabel.pack()
        plotlabel.place(x=20, y=60, relheight=0.7, relwidth=0.9)
        plotlabel.image = img

MyGUI()