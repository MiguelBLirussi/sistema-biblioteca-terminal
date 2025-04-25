import sys
import json
from livro import Livro  #importa a classe Livro de outro arquivo

def main():
    #função principal do programa
    biblioteca = []
    while True:
        exibir_menu()
        comando = tarefa_desejada()
        biblioteca = chamar_tarefa(comando,biblioteca)
    
def voltar_menu():
    #função para sinalizar o usuário que o programa voltara ao menu principal
    print("Tarefa finalizada!\nVoltando ao Menu Principal...")
    
def exibir_menu():
    #exibe o menu principal
    print('Gerenciamento de Bilbioteca')
    print('1. Adicionar livro')
    print('2. Listar todos os livros')
    print('3. Buscar livro por título ou autor')
    print('4. Editar livros disponíveis')
    print('5. Salvar')
    print('6. Carregar')
    print('7. Sair')
    
def tarefa_desejada():
    #recebe o o comando do usuário e retorna esse comando
    loop = True
    while loop == True:
        comando = (input('Digite o número da opção desejada: '))
        try:
            comando = int(comando)
            if comando > 0 and comando < 8:
                loop = False
                return comando
            else:
                print("Por favor digite um comando válido...")
                loop = True
        except:
            print("Por favor digite um comando válido...")
            loop = True
            
def adicionar_livro(biblioteca):
    #função para adicionar um novo livro
    print("Vamos adicionar um novo livro")
    titulo = input("Qual o nome do livro?\n")
    autor = input("Perfeito, qual o autor do livro?\n")
    ano = input("De qual ano é o livro?\n")
    livro = Livro(titulo,autor,ano)
    biblioteca.append(livro)
    voltar_menu()
    return biblioteca
    
def listar_livros(biblioteca):
    # lista todos os livros da biblioteca
    if not biblioteca:
        print("Não há livros na biblioteca.")
    else:
        print("Listando Livros:")
        for livro in biblioteca:
            print(livro)  # aqui ele usa o __str__() da classe Livro
    voltar_menu()
    return biblioteca
    
def buscar_livro():
    #função para buscar um livro pelo autor ou título
    print("Buscando Livro...")
    voltar_menu()
    
def editar_livro():
    #função para editar o status do livro disponivel ou emprestado
    print("Editando Livro...")
    voltar_menu()

def salvar(biblioteca):
    # salva a biblioteca em um arquivo JSON
    livros_dict = [livro.to_dict() for livro in biblioteca]
    with open("biblioteca.json", "w") as file:
        json.dump(livros_dict, file, indent=4)
    print("Biblioteca salva com sucesso!")
    voltar_menu()

def fechar_programa():
    #encerra o programa
    print("Fechando o sistema...")
    sys.exit()
    
def carregar_biblioteca(biblioteca):
    # Carrega os livros de um arquivo JSON
    try:
        with open("biblioteca.json", "r") as file:
            livros_dict = json.load(file)
            biblioteca = [Livro.from_dict(livro) for livro in livros_dict]
        print("Biblioteca carregada com sucesso!")
    except FileNotFoundError:
        print("Nenhum arquivo encontrado. Criando uma nova biblioteca.")
    return biblioteca

def chamar_tarefa(comando, biblioteca):
    #recebe o valor de comando e executa a função desejada
    if comando == 1:
        adicionar_livro(biblioteca)
    elif comando == 2:
        listar_livros(biblioteca)
    elif comando == 3:
        buscar_livro()
    elif comando == 4:
        editar_livro()
    elif comando == 5:
        salvar(biblioteca)
    elif comando == 6:
        biblioteca= carregar_biblioteca(biblioteca)
    elif comando == 7:
        fechar_programa()
    return biblioteca # Retorna a biblioteca no caso de nenhuma ação ser tomada
     
if __name__ == "__main__":
    main()
    