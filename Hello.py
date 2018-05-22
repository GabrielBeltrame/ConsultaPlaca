import tkinter as tk
import json

from sinesp_client import SinespClient

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.sinesp_procura(self.Et_placa)

    def create_widgets(self):
        Et_placa = tk.Entry(bg='white')
        Et_placa.pack()
        return Et_placa

    def sinesp_procura(self, placa):
        # aqui dentro ele chama o escreve_widgets
        vetor = []
        sc = SinespClient()
        results = sc.search(placa)
        for result in results.values():
           vetor.append(result)
        for valor in vetor:
            campo = tk.Label(text=vetor.pop())
            campo.pack()

root = tk.Tk()
root.attributes("-topmost", True)
app = Application(master=root)
app.master.title("Placa Sinesp")

app.mainloop()