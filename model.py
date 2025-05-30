# model.py

# Representa o usuário do sistema. 
# Cada um pode receber notificações quando algo acontece.
class Usuario:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

# Esse método é chamado quando o usuário recebe alguma notificação
    def update(self, mensagem):
        print(f"[NOTIFICAÇÃO] {self.nome} recebeu: {mensagem}")