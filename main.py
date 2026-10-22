from datetime import datetime
from usuario import Estudante, Servidor
from equipamento import Estoque

usuarios = []
estoque = Estoque()


def cadastrar_usuario():
    print("\n--- CADASTRO DE USUARIO ---")

    # Validar o nome
    while True:
        nome = input("Digite o nome: ")
        nome = nome.strip() # esse strip ele remove espaços em branco do começo e do fim do texto

        if nome == "":
            print("Nome invalido! O nome nao pode ficar vazio.")
        else:
            break

    # Validar a matricula
    while True: # isso aqui he interessante pois ele roda uma repeticao ate encontrar um break
        matricula = input("Digite a matricula (ex: a2669560): ")

        if (len(matricula) == 8
                and matricula[0] == "a"
                and matricula[1:].isdigit()): # aqui eh pra verificar se todos os espaços apos o vetor[0]=a sao numeros
            break
        else:
            print("Matricula invalida! Use o formato a0000000.")

    # Escolher o tipo de usuario
    print("1 - Estudante")
    print("2 - Servidor")

    tipo_opcao = input("Escolha o tipo de usuario: ")

    if tipo_opcao == "1":
        usuario = Estudante(nome, matricula)
    elif tipo_opcao == "2":
        usuario = Servidor(nome, matricula)
    else:
        print("Tipo de usuario invalido!")
        return

    usuarios.append(usuario)
    print("Usuario cadastrado com sucesso!")


def consultar_usuarios():
    print("\n--- USUARIOS CADASTRADOS ---")

    if len(usuarios) == 0:
        print("Nenhum usuario cadastrado.")
    else:
        for usuario in usuarios:
            print("Nome:", usuario.nome)
            print("Matricula:", usuario.matricula)
            print("Tipo:", usuario.tipo)
            print("Itens emprestados:", len(usuario.itens_emprestados), "/", usuario.limite_itens())
            print("--------------------------")


def buscar_usuario_por_matricula(matricula):
    for u in usuarios:
        if u.matricula == matricula.strip():
            return u
    return None


def consultar_equipamentos():
    estoque.listar()


def realizar_emprestimo():
    print("\n--- REALIZAR EMPRESTIMO ---")
    matricula = input("Digite a matricula do usuario: ")
    usuario = buscar_usuario_por_matricula(matricula)

    if usuario is None:
        print("Usuario nao encontrado! Cadastre o usuario primeiro.")
        return

    if not usuario.pode_pegar():
        print(f"O usuario {usuario.nome} ja atingiu o limite de {usuario.limite_itens()} itens!")
        return

    estoque.listar()
    codigo = input("\nDigite o codigo do equipamento desejado: ")
    item = estoque.buscar(codigo)

    if item is None:
        print("Equipamento nao encontrado.")
        return

    if not item.disponivel:
        print("Equipamento ja esta emprestado no momento.")
        return

    item.disponivel = False
    usuario.itens_emprestados.append(item)
    data_atual = datetime.now().strftime("%d/%m/%Y")
    usuario.historico.append(f"Emprestimo: {item.nome} em {data_atual}")

    print(f"Emprestimo do item '{item.nome}' realizado para {usuario.nome} com sucesso!")


def registrar_devolucao():
    print("\n--- REGISTRAR DEVOLUCAO ---")
    matricula = input("Digite a matricula do usuario: ")
    usuario = buscar_usuario_por_matricula(matricula)

    if usuario is None:
        print("Usuario nao encontrado.")
        return

    codigo = input("Digite o codigo do equipamento a devolver: ")
    item = estoque.buscar(codigo)

    if item and item in usuario.itens_emprestados:
        # Se for bicicleta faz vistoria
        if item.categoria == "bicicleta":
            print("\n[ VISTORIA DE BICICLETA ]")
            pneu = input("Pneus ok? (s/n): ")
            freio = input("Freios ok? (s/n): ")
            print(f"Vistoria registrada (pneu: {pneu}, freio: {freio}).")

        item.disponivel = True
        usuario.itens_emprestados.remove(item)
        data_atual = datetime.now().strftime("%d/%m/%Y")
        usuario.historico.append(f"Devolucao: {item.nome} em {data_atual}")

        print("Devolucao registrada com sucesso!")
    else:
        print("Este equipamento nao consta na lista de emprestimos deste usuario.")


def consultar_historico():
    print("\n--- CONSULTAR HISTORICO ---")
    matricula = input("Digite a matricula do usuario: ")
    usuario = buscar_usuario_por_matricula(matricula)

    if usuario:
        print(f"\nHistorico de {usuario.nome}:")
        if len(usuario.historico) == 0:
            print("Nenhum registro encontrado.")
        else:
            for registro in usuario.historico:
                print("-", registro)
    else:
        print("Usuario nao encontrado.")


# --- LOOP PRINCIPAL DO MENU ---
opcao = -1

while opcao != 0:
    print("\n================================")
    print("       SISTEMA DA ATLETICA")
    print("================================")
    print("1 - Cadastrar usuario")
    print("2 - Consultar usuarios")
    print("3 - Consultar equipamentos")
    print("4 - Realizar emprestimo")
    print("5 - Registrar devolucao")
    print("6 - Consultar historico")
    print("0 - Sair do sistema")

    try:
        opcao = int(input("Escolha uma opcao: "))

    except ValueError:
        print("Opcao invalida! Digite apenas numeros.")
        continue

    if opcao == 1:
        cadastrar_usuario()

    elif opcao == 2:
        consultar_usuarios()

    elif opcao == 3:
        consultar_equipamentos()

    elif opcao == 4:
        realizar_emprestimo()

    elif opcao == 5:
        registrar_devolucao()

    elif opcao == 6:
        consultar_historico()

    elif opcao == 0:
        print("Sistema encerrado!")

    else:
        print("Opcao inexistente! Escolha uma opcao do menu.")
