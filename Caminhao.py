from Veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, placa, ano, capacidade):
        super().__init__(marca, modelo, placa, ano)
        self.__capacidade = capacidade
    def __str__(self):
        retorno = super().__str__()
        return f'''{retorno}
 - Capacidade de carga: {self.__capacidade}'''

#bicudo = Caminhao("Mercedes", "1113", "ABC", 1993, 8150)
#print(bicudo)