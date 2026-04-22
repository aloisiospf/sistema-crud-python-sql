import sqlite3


def conectar():
    return sqlite3.connect("database.db")


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def cadastrar_usuario(nome, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO usuarios (nome, email) VALUES (?, ?)",
        (nome, email)
    )
    conn.commit()
    conn.close()


def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios


def atualizar_usuario(usuario_id, nome, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE usuarios SET nome = ?, email = ? WHERE id = ?",
        (nome, email, usuario_id)
    )
    conn.commit()
    conn.close()


def excluir_usuario(usuario_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (usuario_id,))
    conn.commit()
    conn.close()


def menu():
    criar_tabela()

    while True:
        print("\n1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Atualizar usuário")
        print("4 - Excluir usuário")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            cadastrar_usuario(nome, email)
            print("Usuário cadastrado com sucesso!")
        elif opcao == "2":
            usuarios = listar_usuarios()
            if not usuarios:
                print("Nenhum usuário cadastrado.")
            else:
                for usuario in usuarios:
                    print(usuario)
        elif opcao == "3":
            usuario_id = int(input("ID do usuário: "))
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            atualizar_usuario(usuario_id, nome, email)
            print("Usuário atualizado com sucesso!")
        elif opcao == "4":
            usuario_id = int(input("ID do usuário: "))
            excluir_usuario(usuario_id)
            print("Usuário excluído com sucesso!")
        elif opcao == "5":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
