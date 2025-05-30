# controller.py

# Aqui gerenciamos os usuários e os eventos do sistema.
# É o "Subject" do padrão Observer: quando algo acontece, avisa todo mundo.
from model import Usuario
from notification import NotificacaoFactory

class NotificationController:
    def __init__(self):
        self.usuarios = [] # Quem vai ser notificado
        self.notificacoes = [] # Métodos de notificação ativos

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuário {usuario.nome} registrado com sucesso!")

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return
        print("\nLista de usuários cadastrados:")
        for idx, u in enumerate(self.usuarios, start=1):
            print(f"{idx}. Nome: {u.nome}, Email: {u.email}, Telefone: {u.telefone}")

    def atualizar_usuario(self, indice, novo_nome=None, novo_email=None, novo_telefone=None):
        if indice < 0 or indice >= len(self.usuarios):
            print("Índice inválido.")
            return
        usuario = self.usuarios[indice]
        old_nome = usuario.nome
        old_email = usuario.email
        old_telefone = usuario.telefone
        if novo_nome:
            usuario.nome = novo_nome
        if novo_email:
            usuario.email = novo_email
        if novo_telefone:
            usuario.telefone = novo_telefone
        print(f"Usuário {old_nome} atualizado para Nome: {usuario.nome}, Email: {usuario.email}, Telefone: {usuario.telefone}")
        self.notificar_usuario(usuario, f"Seus dados foram atualizados de Nome: {old_nome}, Email: {old_email}, Telefone: {old_telefone} para Nome: {usuario.nome}, Email: {usuario.email}, Telefone: {usuario.telefone}")

    def deletar_usuario(self, indice):
        if indice < 0 or indice >= len(self.usuarios):
            print("Índice inválido.")
            return
        usuario = self.usuarios.pop(indice)
        print(f"Usuário {usuario.nome} removido com sucesso!")
        self.notificar_usuario(usuario, "Seu cadastro foi removido do sistema.")

    def adicionar_notificacao(self, notificacao):
        self.notificacoes.append(notificacao)

# Aqui é quando algo importante acontece no sistema
# Dispara notificações pra geral
    def evento_ocorrido(self, mensagem):
        print("\n[Evento importante ocorreu! Notificando todos os usuários...]\n")
        for usuario in self.usuarios:
            for notificacao in self.notificacoes:
                notificacao.enviar(usuario, mensagem)
            usuario.update(mensagem)

# Notifica só um usuário específico
    def notificar_usuario(self, usuario, mensagem):
        for notificacao in self.notificacoes:
            notificacao.enviar(usuario, mensagem)
        usuario.update(mensagem)