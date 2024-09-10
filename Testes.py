from Moto import Moto
from Veiculo import Veiculo

#Instanciando a classe moto
moto = Moto("Honda", "Falcon", "ABC", 2005, 400)
print(moto)

#Instanciando a classe veículo
cerato = Veiculo("Kia", "Cerato", "IRL", 2011)
print(cerato.__str__())

# Abaixo estou instanciando um objeto da classe Veiculo
meuUno = Veiculo("Fiat", "Uno com escada", "ABC-1234", 2000)
print(meuUno.get_marca)
print(meuUno.calcularTempoUso())
meuUno.__ano = 2010
print(meuUno.calcularTempoUso())

teuFusca = Veiculo("Volks", "Fusca do Itamar", "DEF-", 1995)

#print(meuUno.calcularTempoUso())
#print(teuFusca.calcularTempoUso())

#print("")