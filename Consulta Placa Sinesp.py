from tkinter import Tk, Label, Button, Frame, Entry, Listbox

import json

from sinesp_client import SinespClient

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()

        self.campo_placa = Entry(master, width=15)
        self.campo_placa.grid()

        self.btn = Button(master, command=self.get_placa, text='->')
        self.btn.grid()

        self.lstbox = Listbox(master, width=30, height=5)
        self.lstbox.grid()

    def get_placa(self):
        self.placa = self.campo_placa.get()
        self.sinesp_procura(self.placa)

    def sinesp_procura(self, placa_sinesp):
        # aqui dentro ele chama o escreve_widgets
        vetor = []
        sc = SinespClient()
        results = sc.search(placa_sinesp)
        for result in results.values():
           vetor.append(result)
            #fazer um foreach para deletar cada campo
        self.lstbox.delete(0,5)
        self.lstbox.insert(6, vetor[6])
        self.lstbox.insert(7, vetor[7])
        self.lstbox.insert(8, vetor[8])
        self.lstbox.insert(12, vetor[12])
        self.lstbox.insert(13, vetor[13])

        self.lstbox.grid()

root = Tk()
root.attributes("-topmost", True)
app = Application(master=root)
app.master.geometry("200x200")
app.master.title("Placa Sinesp")

app.mainloop()