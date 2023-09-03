import json

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")
    curso = input("Digite o curso do aluno: ")

    aluno = {
        'nome': nome,
        'email': email,
        'curso': curso
    }

    with open('alunos.json', 'a') as arquivo:
        json.dump(aluno, arquivo)
        arquivo.write('\n')

def listar_alunos():
    try:
        with open('alunos.json', 'r') as arquivo:
            for linha in arquivo:
                aluno = json.loads(linha)
                print(f"Nome: {aluno['nome']}, Email: {aluno['email']}, Curso: {aluno['curso']}")
    except FileNotFoundError:
        print("Nenhum aluno cadastrado.")

def buscar_aluno():
    nome_busca = input("Digite o nome do aluno que deseja buscar: ")
    encontrado = False

    try:
        with open('alunos.json', 'r') as arquivo:
            for linha in arquivo:
                aluno = json.loads(linha)
                if aluno['nome'].lower() == nome_busca.lower():
                    print(f"Nome: {aluno['nome']}, Email: {aluno['email']}, Curso: {aluno['curso']}")
                    encontrado = True
    except FileNotFoundError:
        print("Nenhum aluno cadastrado.")

    if not encontrado:
        print("Aluno não encontrado.")

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Cadastrar um novo aluno")
        print("2. Listar os alunos cadastrados")
        print("3. Buscar um aluno pelo nome")
        print("4. Sair")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            buscar_aluno()
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")


main()