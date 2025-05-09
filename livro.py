from datetime import datetime
agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Livro:
    #Atributos da classe
    
    _id_counter = 1000
    
    def __init__(self, titulo, autor, ano):
        self.id = Livro._id_counter
        Livro._id_counter += 1
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True
    
    def __str__(self):
        return f'ID:{self.id} | Título:{self.titulo}| Autor:{self.autor}| Ano:{self.ano}| Disponivel:{'✅' if self.disponivel else '❌'}'
    
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print("Emprestando Livro...")
            return True
        return False
      
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            
            print("Devolvendo Livro...")
        else:
            print("Você não pode devolver esse livro, ele não estava emprestado...")
            
    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'autor': self.autor,
            'ano': self.ano,
            'disponivel': self.disponivel
        }

    @classmethod
    def from_dict(cls, dados):
        livro = cls(dados["titulo"], dados["autor"], dados["ano"])
        livro.disponivel = dados["disponivel"]
        # Se o JSON tem 'id', usa ele; senão, cria um novo automaticamente
        if "id" in dados:
            livro.id = dados["id"]
            # Mantém o controle de IDs únicos
            if dados["id"] >= Livro._id_counter:
                Livro._id_counter = dados["id"] + 1
        return livro
        