class Search_plate():

    def procura_placa(placa_sinesp):
        vetor = []
        sc = SinespClient()
        results = sc.search(placa_sinesp)
        for result in results.values():
            vetor.append(result)

        # limpar listbox
        Application.apaga_lstbox()
        Application.escreve_lstbox(vetor)

        # Criar Contador
        # self.qtd_pesquisas_label(qtd+1)
        # Application.lstbox.grid()

    def contador(self):
        print("É chamada quando é feito uma pesquisa")

        def __init__(self):
            qtd_pesquisa = 0

        def set_qtd(self):
            qtd_pesquisa + +1

        def get_qtd(self):
            return qtd_pesquisa