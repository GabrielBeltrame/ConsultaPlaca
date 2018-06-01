import tkinter as tk

from sinesp_client import SinespClient

class Application(tk.Frame):

    #Construtor da tela
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("272x144")
        self.root.attributes("-topmost", True)

        tk.Frame.__init__(self, self.root)
        self.create_widgets()

    def create_widgets(self):
        self.root.bind('<Return>', self.get_placa)
        self.grid()

        self.campo_placa = tk.Entry(self, width=15) #Entry(master, width=15)
        self.campo_placa.grid()

        self.submit = tk.Button(self, text="Submit")
        self.submit.bind('<Button-1>', self.get_placa)
        self.submit.grid()

        self.lstbox = tk.Listbox(self, width=30, height=5)
        self.lstbox.grid()

    # pega a placa a ser pesquisado escrita no Entry pelo usuario
    def get_placa(self, event):
        placa = self.campo_placa.get()
        sc = SinespClient()
        results = sc.search(placa)
        self.apaga_lstbox()
        self.escreve_lstbox(results)

    def apaga_lstbox(self):
        self.lstbox.delete(0,5)

    def escreve_lstbox(self,valor):
        if valor["return_code"] == '3':
            self.lstbox.insert(0,valor["return_message"])
        else:
            self.lstbox.insert(0,valor["model"])
            self.lstbox.insert(1,valor["color"])
            self.lstbox.insert(2,valor["year"])
            self.lstbox.insert(3,valor["state"])
            self.lstbox.insert(4,valor["city"])

    def start(self):
        self.root.mainloop()

Application().start()
