class Carro():

    def __init__(self, placa, modelo, cor, ano_fabricacao, ano_modelo,estado, cidade, status, retorno_sinesp):
        self.__placa = placa
        self.__modelo = modelo
        self.__cor = cor
        self.__ano_fabricacao = ano_fabricacao
        self.__ano_modelo = ano_modelo
        self.__estado = estado
        self.__cidade = cidade
        self.__status = status
        self.__retorno_sinesp = retorno_sinesp


    # <editor-fold desc="Gets">
    @property
    def placa(self):
        return self.__placa

    @property
    def modelo(self):
        return self.__modelo

    @property
    def cor(self):
        return self.__cor

    @property
    def ano_fabricacao(self):
        return self.__ano_fabricacao

    @property
    def estado(self):
        return self.__estado

    @property
    def cidade(self):
        return self.__cidade

    @property
    def status(self):
        return self.__status

    @property
    def retorno_sinesp(self):
        return self.__retorno_sinesp
    # </editor-fold>

