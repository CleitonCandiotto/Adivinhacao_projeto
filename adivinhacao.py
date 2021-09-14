from random import randint


print('=-=' * 10)
print(f'{"ADIVINHAÇÂO":^30}')
print('=-=' * 10)


class ChuteNumero:
    def __init__(self):
        self.tentativas = 10
        self.valor_do_chute = 0
        self.__aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    @property
    def aleatorio(self):
        return self.__aleatorio

    @aleatorio.setter
    def aleatorio(self, novo_numero):
        self.aleatorio = novo_numero

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        try:
            self.PedirValorAleatorio()
            while self.tentar_novamente:
                if self.valor_do_chute > self.aleatorio:
                    print('Chute um valor mais baixo')
                    self.tentativas -= 1
                    print(f'Tentativas Restantes: {self.tentativas}')
                    self.PedirValorAleatorio()
                elif self.valor_do_chute < self.aleatorio:
                    print('Chute um valor mais alto')
                    self.tentativas -= 1
                    print(f'Tentativas Restantes: {self.tentativas}')
                    self.PedirValorAleatorio()
                if self.valor_do_chute == self.aleatorio:
                    self.tentar_novamente = False
                    print('Parabens, você acertou!!')
                if self.tentativas == 1:
                    self.tentar_novamente = False
                    print('Acabaram as tentativas')
        except:
            print('Apenas Numeros')
            self.Iniciar()

    def PedirValorAleatorio(self):
        self.valor_do_chute = int(input('Chute um número: '))

    def GerarNumeroAleatorio(self):
        self.__aleatorio = randint(self.valor_minimo, self.valor_maximo)


chute = ChuteNumero()
chute.Iniciar()
