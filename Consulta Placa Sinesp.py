from tkinter import Tk, Label, Button, Frame, Entry, Listbox

import json

from sinesp_client import SinespClient

class Application(Frame):

    #Construtor da tela
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()

        self.campo_placa = Entry(master, width=15)
        self.campo_placa.grid()

        self.btn = Button(master, command=self.get_placa, text='->')
        self.btn.grid()

        self.lstbox = Listbox(master, width=30, height= 5)
        self.lstbox.grid()

        self.qtd_pesquisas_label = Label(master, text=qtd_pesquisa)
        self.qtd_pesquisas_label.grid()

    # pega a placa a ser pesquisado escrita no Entry pelo usuario
    def get_placa(self):
        sinesp.procura_placa(self.campo_placa.get())
        conta.set_qtd(qtd_pesquisa)

    def apaga_lstbox(self):
        self.lstbox.delete(0,5)

    def escreve_lstbox(self, vetor):
        self.lstbox.insert(6, vetor[6])
        self.lstbox.insert(7, vetor[7])
        self.lstbox.insert(8, vetor[8])
        self.lstbox.insert(12, vetor[12])
        self.lstbox.insert(13, vetor[13])

class sinesp():

    def procura_placa(placa_sinesp):
        vetor = []
        sc = SinespClient()
        results = sc.search(placa_sinesp)
        for result in results.values():
            vetor.append(result)

        #limpar listbox
        Application.apaga_lstbox()
        Application.escreve_lstbox(vetor)

        # Criar Contador
        # self.qtd_pesquisas_label(qtd+1)
        #Application.lstbox.grid()

class conta():
    print("É chamada quando é feito uma pesquisa")
    def __init__(self):
        qtd_pesquisa = 0

    def set_qtd(self):
        qtd_pesquisa++1

    def get_qtd(self):
        return  qtd_pesquisa


root = Tk()
root.attributes("-topmost", True)
app = Application(master=root)
app.master.geometry("200x200")
app.master.title("Placa Sinesp")

app.mainloop()
