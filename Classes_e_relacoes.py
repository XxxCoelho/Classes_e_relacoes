# Atividade: Associação, Agregação e Composição.

class Carro:
    def __init__(self, nome):
        self._nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def nome(self):
        return self._nome

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

    def Dar_partida(self):
        if self.fabricante is None:
            raise ValueError(f'O {self._nome} não possui motor para dar partida!')
        if not self.fabricante:
            print(f'O {self._nome} já esta ligado!')
            return
        print(f'O {self._nome} deu partida')


class Motor:
    def __init__(self, nome, modelo):
        self._nome = nome
        self._modelo = modelo

    @property
    def nome(self):
        return self._nome

    @property
    def modelo(self):
        return self._modelo


class Fabrica:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome


Celta = Carro('Celta')
V6 = Motor('V6', '6 canecos')
Fiate = Fabrica('Fiate')

Celta.motor = V6
Celta.fabricante = Fiate

print(f'Nome: {Celta.nome}, Motor: {Celta.motor.nome}, Fabricante: {Celta.fabricante.nome}')
