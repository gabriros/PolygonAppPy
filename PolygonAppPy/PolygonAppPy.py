import tkinter as tk
import random
from tkinter import *
from tkinter import colorchooser
from tkinter.colorchooser import askcolor
from PIL import Image, ImageTk

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight = 1)
        container.columnconfigure(0, weight = 1)

        self.frames = {}
        for F in (MenuPage, OptionsPage, GamePage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.show_frame(MenuPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)

        logo = Image.open('logo.png')
        resizedLogo = logo.resize((442,100), Image.ANTIALIAS)
        newLogo = ImageTk.PhotoImage(resizedLogo)
        logo_label = tk.Label(self, image = newLogo)
        logo_label.image = newLogo
        
        #buttons
        gameButton = tk.Button(self, text="Play", command=lambda: controller.show_frame(GamePage), width=10)
        optionsButton = tk.Button(self, text="Options", command=lambda: controller.show_frame(OptionsPage))
        exitButton = tk.Button(self, text="Exit", command=self.quit)
        
        #show Items
        logo_label.grid(row=0, column=0, pady=20, padx=0)
        gameButton.grid(row=1, column=0, pady=(50,0), padx=0)
        optionsButton.grid(row=2, column=0, pady=100, padx=0)
        exitButton.grid(row=3, column=0, pady=(0,100), padx=0)

class OptionsPage(tk.Frame):
        
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width=600, height=300)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        def change_color():
            colors = askcolor(title="Background Color Chooser")
            self.configure(bg=colors[1])
            #MenuPage.config.
            #frame = MenuPage (self.configure(bg=colors[1]))
            #menuPage.configure(bg=colors[1])
            #Frame.configure(bg=colors[1])
            #GamePage.configure()

        #buttons
        backgroundButton = tk.Button(self, text="Background color", command=change_color)
        optBackButton = tk.Button(self, text="Back", command=lambda: controller.show_frame(MenuPage))

        #show Items
        backgroundButton.grid(column=0, row=0)
        optBackButton.grid(column=0, row=1)


class GamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        l = tk.IntVar();

        #Items
        c = Canvas(self, bg="white", height=1000, width=2000)    
        gameBackButton = tk.Button(self, text="Back", command=lambda: controller.show_frame(MenuPage))
        rectangle = tk.Radiobutton(self, text="Rectangle", variable=l, value=0, command=lambda: print(l.get()))
        triangle = tk.Radiobutton(self, text="Rectangle", variable=l, value=0, command=lambda: print(l.get()))

        #show Items
        c.grid(sticky="W", row=0, column=0, padx=30, pady=30)
        rectangle.grid(sticky="W", row=1, column=0, padx=30, pady=(30,0))
        triangle.grid(sticky="W", row=2, column=0, padx=30, pady=20)
        gameBackButton.grid(sticky="E", row=2, column=1, padx=80, pady=40)

app = Application()
app.overrideredirect(True)
app.overrideredirect(False)
app.attributes('-fullscreen',True)
app.mainloop()
