from Veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, marca, modelo, placa, ano, cilindradas):
        super().__init__(marca, modelo, placa, ano)
        self.__cilindradas = cilindradas
    
    def __str__(self):
        retorno = super().__str__()
        return f'''{retorno}
 - Cilindradas: {self.__cilindradas}'''

