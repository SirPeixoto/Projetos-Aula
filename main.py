from Livros import Livros

def cadastrar_livro(lista):
    codigo = input(f'Código do livro: ')
    titulo = input(f'Título: ')
    editora = input(f'Editora: ')
    categoria = input(f'Categoria: ')
    ano = input(f'Ano: ')
    valor = float(input(f'Valor: '))
    estoque = int(input(f'Quantidade em estoque: '))
    lista.append(Livros(codigo, titulo, editora, categoria, ano, valor, estoque))
    print()
    print('Livro cadastrado!')

def listar_livros(lista):
    if lista:
        for livro in lista:
            livro.info()
    if not lista:
        print()
        print('Nenhum livro encontrado.')

def buscar_nome(lista):
    titulo = input("Digite o título do livro: ").lower()
    encontrados = []
    for livro in lista:
        if titulo in livro.titulo.lower():
            encontrados.append(livro)
    if encontrados:
        for livro in encontrados:
            livro.info()
    else:
        print()
        print('Livro não encontrado!')
        
def buscar_por_categoria(lista):
    area = input("Digite a área do livro: ").lower()
    encontrados = []
    for livro in lista:
        if area in livro.area.lower():
            encontrados.append(livro)
    if encontrados:
        for livro in encontrados:
            livro.info()
    else:
        print()
        print('Nenhum resultado encontrado!')

def buscar_por_preco(lista):
    preco_max = float(input("Digite o preço máximo: "))
    encontrados = []
    for livro in lista:
        if livro.valor < preco_max:
            encontrados.append(livro)
    if encontrados:
        for livro in encontrados:
            livro.info()
    else:
        print()
        print("Nenhum livro encontrado abaixo deste preço.")

def buscar_por_estoque(lista):
    estoque_min = int(input("Digite a quantidade mínima em estoque: "))
    encontrados = [livro for livro in lista if livro.estoque > estoque_min]
    for livro in lista:
        if livro.estoque > estoque_min:
            encontrados.append(livro)
    if encontrados:
        for livro in encontrados:
            livro.info()
    else:
        print()
        print("Nenhum livro encontrado com essa quantidade.")

def valor_total_estoque(lista):
    total = sum(livro.valor * livro.estoque for livro in lista)
    print(f"O valor total em estoque é: R${total:.2f}\n")

def menu(lista):
    print()
    while True:
        print()
        print(f'1 - Cadastrar novo livro')
        print(f'2 - Listar Livros')
        print(f'3 - Buscar livros por nome')
        print(f'4 - Buscar livros por categoria')
        print(f'5 - Buscar livros por preço')
        print(f'6 - Busca por quantidade em estoque')
        print(f'7 - Valor total em estoque')
        print(f'0 - Encerrar atividades')
        print()

        opcao = input('Digite a opção:')
        print()

        if opcao == '1':
            cadastrar_livro(lista)
        elif opcao == '2':
            listar_livros(lista)
        elif opcao == '3':
            buscar_nome(lista)
        elif opcao == '4':
            buscar_por_categoria(lista)
        elif opcao == '5':
            buscar_por_preco(lista)
        elif opcao == '6':
            buscar_por_estoque(lista)
        elif opcao == '7':
            valor_total_estoque(lista)
        elif opcao == '0':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == '__main__':
    lista = [
        Livros('0301', 'Compiladores', 'Pearson', 'Computação', 2016, 85.00, 125),
        Livros('1203', 'Engenharia de Software', 'Pressman', 'Computação', 2011, 78, 100)
    ]
    menu(lista)