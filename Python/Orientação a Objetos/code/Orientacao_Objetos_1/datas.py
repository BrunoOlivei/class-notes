class Data:

    def __init__(self):
        data = input('Digite a data de nascimento: ')
        data_formatada = data.split("/")
        self.__dia = int(data_formatada[0])
        self.__mes = int(data_formatada[1])
        self.__ano = int(data_formatada[2])


    def imprime_data(self):
        if self.__dia < 10:
            print(f'0{self.__dia}/{self.__mes}/{self.__ano}')
        else:
            print(f'{self.__dia}/{self.__mes}/{self.__ano}')
