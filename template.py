import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image


class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x600")

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

        self.label = tk.Label(self.root, text='message', font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text='show message', font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.btn = tk.Button(self.root, text='Show', font=('Arial', 16), command=self.show_message)
        self.btn.pack(padx=10, pady=10)

        self.plot_button = tk.Button(self.root, command = self.plot, height=2, width=10, text = "Plot")
        self.plot_button.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.onclosing)
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
        img = ImageTk.PhotoImage(Image.open("image.png").resize([50, 50]))
        label1 = tk.Label(self.root, image=img, height=50, width=50)
        label1.image = img
        label1.pack()
        label1.place(x=10, y=400)

MyGUI()