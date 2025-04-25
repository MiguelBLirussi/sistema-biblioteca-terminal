class Livro:
    #Atributos da classe
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True
        
    def __str__(self):
        return f'Título:{self.titulo}| Autor:{self.autor}| Ano:{self.ano}| Disponivel:{self.disponivel}'
    
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print("Emprestando Livro...")
        else:
            print("O livro não está disponivel...")
            
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print("Devolvendo Livro...")
        else:
            print("Você não pode devolver esse livro, ele não estava emprestado...")
            
    def to_dict(self):
        return{
        'titulo': self.titulo,
        'autor': self.autor,
        'ano': self.ano,
        'disponivel': self.disponivel
        }
        
    @classmethod
    def from_dict(cls, dados):
        livro = cls(dados["titulo"], dados["autor"], dados["ano"])
        livro.disponivel = dados["disponivel"]
        return livro
        