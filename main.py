# main.py

# Aqui rola a interação com o usuário. É a "View" do MVC.
from model import Usuario
from controller import NotificationController
from notification import NotificacaoFactory

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o e-mail do usuário: ")
    telefone = input("Digite o telefone do usuário: ")
    return Usuario(nome, email, telefone)

def escolher_notificacoes():
    notificacoes = []
    print("Escolha os tipos de notificação que deseja adicionar:")
    print("1 - E-mail")
    print("2 - SMS")
    print("3 - Ambos")
    opcao = input("Digite a opção: ")

    if opcao == "1":
        notificacoes.append(NotificacaoFactory.criar_notificacao("email"))
    elif opcao == "2":
        notificacoes.append(NotificacaoFactory.criar_notificacao("sms"))
    elif opcao == "3":
        notificacoes.append(NotificacaoFactory.criar_notificacao("email"))
        notificacoes.append(NotificacaoFactory.criar_notificacao("sms"))
    else:
        print("Opção inválida! Nenhuma notificação foi adicionada.")

    return notificacoes

def main():
    sistema = NotificationController()

    print("=== Sistema de Notificações ===")
    
    while True:
        print("\n1 - Cadastrar novo usuário")
        print("2 - Listar usuários")
        print("3 - Atualizar usuário")
        print("4 - Deletar usuário")
        print("5 - Disparar evento")
        print("6 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            usuario = cadastrar_usuario()
            sistema.registrar_usuario(usuario)

            notificadores = escolher_notificacoes()
            for notificador in notificadores:
                sistema.adicionar_notificacao(notificador)

        elif escolha == "2":
            sistema.listar_usuarios()

        elif escolha == "3":
            sistema.listar_usuarios()
            if sistema.usuarios:
                try:
                    idx = int(input("Digite o número do usuário que deseja atualizar: ")) - 1
                    novo_nome = input("Digite o novo nome (ou deixe vazio para manter): ").strip()
                    novo_email = input("Digite o novo e-mail (ou deixe vazio para manter): ").strip()
                    novo_telefone = input("Digite o novo telefone (ou deixe vazio para manter): ").strip()

                    novo_nome = novo_nome if novo_nome else None
                    novo_email = novo_email if novo_email else None
                    novo_telefone = novo_telefone if novo_telefone else None

                    sistema.atualizar_usuario(idx, novo_nome, novo_email, novo_telefone)
                except ValueError:
                    print("Entrada inválida. Tente novamente.")

        elif escolha == "4":
            sistema.listar_usuarios()
            if sistema.usuarios:
                try:
                    idx = int(input("Digite o número do usuário que deseja deletar: ")) - 1
                    sistema.deletar_usuario(idx)
                except ValueError:
                    print("Entrada inválida. Tente novamente.")

        elif escolha == "5":
            msg = input("Digite a mensagem do evento: ")
            sistema.evento_ocorrido(msg)

        elif escolha == "6":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()