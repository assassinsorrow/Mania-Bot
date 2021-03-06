import tkinter as tk
from tkinter import ttk, Entry, messagebox
from Core import Gui


# this isnt in modules because it is related to ui and not "back end"
class Settings:
    def __init__(self, running):
        if running in [False, None]:
            # this is  so bad
            self.masters = tk.Tk()
            canvas = tk.Canvas(self.masters)
            self.masters.geometry("500x500")
            self.masters.title(u"Settings")
            # creates widgets
            self.Create_Widgets()
            self.masters.config(bg="#333333")
            self.masters.resizable(width=False, height=False)
            self.masters.attributes("-alpha", 0.965)
            self.masters.wait_visibility()
            ttk.Style().configure("TP.TFrame", background="snow")
            Gui.CenterWin(self.masters)
            self.masters.mainloop()
        else:
            messagebox.showwarning(
                "Bot is running",
                "The Bot is running please stop Bot before changing settings",
            )

    def Create_Widgets(self):
        pass
