# notification.py

# Aqui definimos os tipos de notificação (email e SMS)
# E usamos um Factory pra instanciar os tipos de forma flexível
from abc import ABC, abstractmethod

# Interface base pra qualquer tipo de notificação
class Notificacao(ABC):
    @abstractmethod
    def enviar(self, usuario, mensagem):
        pass

class NotificacaoEmail(Notificacao):
    def enviar(self, usuario, mensagem):
        print(f"Email enviado para {usuario.email}: {mensagem}")

class NotificacaoSMS(Notificacao):
    def enviar(self, usuario, mensagem):
        print(f"SMS enviado para {usuario.telefone}: {mensagem}")

# Cria o tipo de notificação conforme informado (Factory Method aplicado aqui)
class NotificacaoFactory:
    @staticmethod
    def criar_notificacao(tipo):
        if tipo == "email":
            return NotificacaoEmail()
        elif tipo == "sms":
            return NotificacaoSMS()
        else:
            raise ValueError("Tipo de notificação inválido.")