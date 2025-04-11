class Livros:
    def __init__(self, codigo, titulo, editora, area, ano, valor, estoque):
        self.codigo = codigo
        self.titulo = titulo
        self.editora = editora
        self.area = area
        self.ano = ano
        self.valor = valor
        self.estoque = estoque
        
    def info(self):
        print()
        print(f'>>>>>Cod#{self.codigo}')
        print(f'Titulo/Editora: {self.titulo}/{self.editora}')
        print(f'Categoria: {self.area}')
        print(f'Ano: {self.ano}')
        print(f'Valor: R${self.valor:.2f}')
        print(f'Estoque: {self.estoque} unidades')
        print(f'Valor total em estoque: R${self.valor * self.estoque:.2f}')
        print()