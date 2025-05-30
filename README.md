# 🔔 Sistema de Notificações em Python

Este é um sistema simples de notificações para usuários, feito como parte de um trabalho da disciplina **Engenharia de Software 2** (UEMG), com foco na aplicação de padrões de projeto e organização em camadas **MVC**.

---

## 💡 Objetivo

Criar um sistema que:

- Cadastre usuários com nome, e-mail e telefone.
- Notifique todos os usuários sempre que um evento importante ocorrer.
- Suporte múltiplos métodos de notificação (e-mail, SMS etc.).
- Permita incluir novos tipos de notificação sem alterar o núcleo do sistema.

---

## 🧠 Padrões de Projeto Utilizados

### 📌 Observer
> Aplicado para notificar automaticamente todos os usuários cadastrados sempre que ocorre um evento.

- A classe `NotificationController` atua como o **Subject**.
- A classe `Usuario` atua como o **Observer**.
- Quando um evento ocorre, o controller dispara notificações para todos os usuários registrados.

### 📌 Factory Method
> Usado para criar os tipos de notificação de forma flexível e escalável.

- A classe `NotificacaoFactory` gera instâncias de `NotificacaoEmail` e `NotificacaoSMS` com base no tipo passado.
- Isso facilita a adição de novos canais de notificação no futuro sem modificar a lógica principal.

---

## 📐 Estrutura do Projeto (MVC)

- `main.py` → View (interface de interação via terminal)
- `controller.py` → Controller (lógica principal e controle de fluxo)
- `model.py` → Model (representação do usuário)
- `notification.py` → Tipos de notificações e Factory Method
