dias = {}

def adicionarDias(posicao, dia):
    if(posicao <= 7):
        dias[posicao] = dia
        return dias

def exibirDias():
    for d, v in dias.items():
        print("dia:", d, "nome:", v)

def menu():
    cont = 0
    while(cont <= 7):
        escolha = eval(input("1 para adicionar os dias e 2 para exibir os dias. "))
        cont+=1
        if(escolha == 1):
           posicao = eval(input(" Digite numero do dia: "))
           dia = input(" Digite qual o dia: ")
           adicionarDias(posicao, dia)
        elif(escolha == 2):
           exibirDias()

menu()


