from tkinter import Tk, Label, Button, Frame, Entry
import json

from sinesp_client import SinespClient

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()

        self.campo_placa = Entry(master)
        self.campo_placa.grid()

        self.btn = Button(master, command=self.get_placa, text='->')
        self.btn.grid()


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
        for valor in vetor:
            campo = Label(text=vetor.pop())
            campo.pack()

root = Tk()
root.attributes("-topmost", True)
app = Application(master=root)
app.master.title("Placa Sinesp")

app.mainloop()