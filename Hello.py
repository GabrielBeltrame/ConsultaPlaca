import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        Label_placa = tk.Label(text='Placa:')
        Label_placa.pack()
        Entry_placa = tk.Label(text='XXX9999', bg='white')
        Entry_placa.pack()

root = tk.Tk()
root.attributes("-topmost", True)
app = Application(master=root)
app.master.title("Placa Sinesp")

app.mainloop()