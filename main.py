import sys
import os
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
    print("\nTarefa finalizada!\nVoltando ao Menu Principal...")
    jump = input("Aperte 'Enter' para voltar ao Menu Principal") #Eu sei, isso aqui é uma solução muito burra mas eu vou arrumar posteriormente
    os.system('cls')
        
def exibir_menu():
    #exibe o menu principal
    print('Gerenciamento de Biblioteca')
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
        jump = input("Aperte 'Enter' para continuar.") #Eu sei isso aqui é uma solução muito burra mas eu vou arrumar posteriormente
    voltar_menu()
    return biblioteca
    
def buscar_livro(biblioteca): 
    while True: #inicio de loop para tratar exceções
        print("Buscando Livro...")
        comando = input("Você deseja procurar pelo título do livro ou pelo autor?\n 1. Título | 2. Autor | 3. Sair para o Menu\n")
        try:
            comando = int(comando)
            if comando == 1:
                titulo = input("Qual o título do livro que está procurando?\n").strip().lower()
                encontrados = list(filter(lambda livro: titulo in livro.titulo.strip().lower(), biblioteca)) #percorre a biblioteca com a função filter dentro dela procura pelo livro com o mesmo titulo
                if encontrados:
                    print("\nLivro(s) encontrado(s):")
                    for livro in encontrados:
                        print(livro)
                else:
                    print("\nNenhum livro encontrado com esse título.")
                break
            elif comando == 2:
                autor = input("Qual o autor que está procurando?\n").strip().lower()
                encontrados = list(filter(lambda livro: autor in livro.autor.strip().lower(), biblioteca)) #mesma coisa porem com o autor
                if encontrados:
                    print("\nLivro(s) encontrado(s):")
                    for livro in encontrados:
                        print(livro)
                else:
                    print("\nNenhum livro encontrado com esse autor.")
                break
            elif comando == 3:
                voltar_menu()
                break
            else:
                print("Digite uma opção válida")
        except ValueError:
            print("Digite uma opção válida")
    voltar_menu()

def editar_livro(biblioteca):
    #função para editar o status do livro disponivel ou emprestado
    id = input("Digite o ID do livro que deseja editar: ")
    try:
        int(id)
        for livro in biblioteca:
            if id == livro.id:
                print("Editando Livro...")
                livro.disponivel = not livro.disponivel
    except ValueError:
        print("Digite um ID válido")
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
    voltar_menu()
    return biblioteca

def chamar_tarefa(comando, biblioteca):
    #recebe o valor de comando e executa a função desejada
    if comando == 1:
        adicionar_livro(biblioteca)
    elif comando == 2:
        listar_livros(biblioteca)
    elif comando == 3:
        buscar_livro(biblioteca)
    elif comando == 4:
        editar_livro(biblioteca)
    elif comando == 5:
        salvar(biblioteca)
    elif comando == 6:
        biblioteca= carregar_biblioteca(biblioteca)
    elif comando == 7:
        fechar_programa()
    return biblioteca # Retorna a biblioteca no caso de nenhuma ação ser tomada
     
if __name__ == "__main__":
    main()
    