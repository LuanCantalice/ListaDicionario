produtos = {}

def cadastrarProduto(produto, preco):
    produtos[produto] = preco
    return produtos

def exibirProdutos():
    print("\nProdutos cadastrados: ")
    for c, v in produtos.items():
        print("Produto:", c, "Preco:", v)

def removerProduto (produtoRemove):
    produtos.pop(produtoRemove)
    print("\n produto removido.")

def exibirCaroProduto():
    maiscaro = max(produtos.keys())
    print("\n O produto mais caro é o: ", maiscaro)

def exibirBaratoProduto():
    maisbarato = min(produtos.keys())
    print("\n O produto mais barato é o: ", maisbarato)
    

def menu():
    cont = 0
    while(cont == 0):
        escolha = eval(input("\n-1 para cadastrar um produto \n-2 para exibi-los \n-3 para remover algum produto \n-4 para exibir o mais caro \n-5 para exibir o mais barato \n-6 para sair.\n"))
        if(escolha == 1):
            produto = input("\n Digite o produto:   ")
            preco = float(input(" Digite o preco desse produto:   "))
            cadastrarProduto(produto, preco)
        elif(escolha == 2):
            exibirProdutos()
        elif(escolha == 3):
            produtoRemove = input("\n Digite o produto a ser removido:   ")
            removerProduto(produtoRemove)
        elif(escolha == 4):
            exibirCaroProduto()
        elif(escolha == 5):
            exibirBaratoProduto()
        else:
            cont = 1

menu()
            
