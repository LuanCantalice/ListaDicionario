funcionarios = {}

def adicionarFuncionario(matricula, nome):
    funcionarios[matricula] = nome
    return funcionarios

def buscarFuncionarios(matriculaBusca):
    for m, n in funcionarios.items():
        if(m == matriculaBusca):
            print(" funcionario encontrado -> ", n, "\n matricula -> ", m)
            return
    print("\n funcionario inexistente")
            
    
        
def exibirFuncionarios(funcionarios):
    print("\n Funcionarios cadastrados: ")
    for m, f in funcionarios.items():
        print("\n Matricula=", m, "\n Nome=", f)

def menu():
    cont = 0
    while(cont == 0):
        escolha = eval(input(" \n 1 para adicionar funcionarios \n 2 para buscar um funcionario \n 3 para exibir os funcionarios \n 4 para sair do programa.\n"))
        if(escolha == 1):
            matricula = input("digite a matricula do funcionario:   ")
            nome = input("digite o nome do funcionario:    ")
            adicionarFuncionario(matricula, nome)
        elif(escolha == 2):
            matriculaBusca = input(" \n digite a matricula do funcionario:   ")
            buscarFuncionarios(matriculaBusca)
        elif(escolha == 3):
            exibirFuncionarios(funcionarios)
        elif(escolha == 4):
            cont = 1
        else:
            print("não existe esta opcao")

menu()
