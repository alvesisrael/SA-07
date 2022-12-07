reserv_pessoa = {}
select_aviao = None
class fly:

    def __init__(self,assento):
        self.reserva_dicio = {}
        for i in range(assento):
            self.reserva_dicio[i] = "Assento disponivel."

    def reservar(self, select_aviao):
        assentos_disp = 0
        for i in range(len(self.reserva_dicio)):
            if self.reserva_dicio[i] == "Assento disponivel.":
                assentos_disp += 1
        if assentos_disp > 0:
            print(f"Os assentos são {self.reserva_dicio}") 
            nome = input("Digite o nome do passageiro: \n")
            nAssento = int(input("Digite o numero do assento para reservar: "))
            if self.reserva_dicio[nAssento] == "Assento disponivel.":
                self.reserva_dicio[nAssento] = f"Assento reservado por {nome}"
                reserv_pessoa[f"aviao nº {select_aviao}, assento Nº{nAssento}"] = nome
                print(self.reserva_dicio[nAssento])
            else:
                print("Esse assento ja esta reservado.. ")
        else:
            print("Não há assento disponiveis para esse avião.. ")

    def mostrar(self):
        if all(assento == "Assento disponivel." for assento in self.reserva_dicio.values()):
            print("Não foram realizadas nenhuma reserva para ester avião.")
        else:
            return self.reserva_dicio




def opcao():
    print("Selecione opção: ")
    print("Escolha opção [1] - Registrar número de avião:")
    print("Escolha opção [2] - Registrar o quantitativo de assentos disponíveis em cada avião:")
    print("Escolha opção [3] - Reservar passagem aérea:")
    print("Escolha opção [4] - Realizar consulta por avião:")
    print("Escolha opção [5] - Realizar consulta por passageiro:")
    print("Escolha opção [6] - Encerrar:")
    opcao_selecionada = int(input("opção: "))
    return opcao_selecionada

def opcao1():
    avioes = []
    for i in range(2):
        avioes2 = int(input("Digite o numero do avião: \n"))
        avioes.append(avioes2)
    return avioes 
avioes = []        

def opcao2(avioes):
    dicionario_ob = {}    
    for i in range(2):
        assento = int(input("Digite quantidade de assentos que quer registrar. \n"))
        try:
            dicionario_ob [avioes[i]] = fly(assento)
        except:
            raise TypeError("Apenas numeros inteiros. ")
    return dicionario_ob

dicionario_ob = {}

def dispo():
    disp = []
    key = list (dicionario_ob)
    for i in range(len(dicionario_ob)):
        if dicionario_ob[key[i]] != "":
            disp.append(key[i])
    return disp

def opcao3(dicionario_ob):
    disp = dispo()
    print(f"Os aviões disponiveis são: {disp}")
    select_aviao = int(input("Digite o numero do avião: \n"))
    if select_aviao in disp:
        dicionario_ob[select_aviao].reservar(select_aviao)
    else:
        print("Esse avião não existe.")
    return select_aviao




def opcao4():
    disp = dispo()
    print(f"Os aviões disponiveis são {disp}")
    select_aviao = int(input("Digite o numero do avião: \n"))
    if select_aviao in disp:
        print(dicionario_ob[select_aviao].mostrar())
    else:
        print("Esse avião não existe.")    

def opcao5():
    nome = input("Digite o nome do passageiro: \n")
    reserva = [assento for assento in reserv_pessoa if reserv_pessoa[assento] == nome]
    print("os assentos reservados por esse passageiro são:")
    if len(reserva) == 0:
        print("não há reservas realizadas para esse passageiro")
    else:
        print(reserva)

opcao_selecionada = opcao()

while opcao_selecionada != 6:
    if  opcao_selecionada == 1:
        avioes = opcao1()
        opcao_selecionada = opcao()
    elif opcao_selecionada == 2:
        dicionario_ob = opcao2(avioes)
        opcao_selecionada = opcao()
    elif opcao_selecionada == 3:
        opcao3(dicionario_ob)
        opcao_selecionada = opcao()
    elif opcao_selecionada == 4:
        opcao4()
        opcao_selecionada = opcao()
    elif opcao_selecionada == 5:
        opcao5()
        opcao_selecionada = opcao()
    else:
        print("Opção inválida. ")
        opcao_selecionada = opcao()
print("Programa finalizado. ")

