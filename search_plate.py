
from sinesp_client import SinespClient

class Search_plate():

    def procura_placa(placa_sinesp):
        vetor = []
        sc = SinespClient()
        results = sc.search(placa_sinesp)
        for result in results.values():
            vetor.append(result)

    #TODO Ainda tenho que repensar se é realmente necessário
    # uma classe apenas para fazer pesquisa
