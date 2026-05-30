# Meu Projeto de API Bancária - Desafio DIO 🚀

Olá! Este é o meu projeto desenvolvido para a trilha de Python da plataforma **DIO** Criei um sistema para um banco que funciona de forma rápida e moderna (chamada de assíncrona).

## 🛠️ O que foi usado no projeto:

* **Python e FastAPI**: As ferramentas principais que usei para construir o sistema e criar os caminhos da nossa API.
* **Pydantic**: Uma biblioteca que ajuda a conferir se as informações enviadas estão certas.
* **Bancos de Dados (SQLite e SQLAlchemy)**: Onde ficam guardadas as informações de contas e do histórico de dinheiro.

## 📌 O que o sistema faz na prática:

* **Segurança**: Protege o sistema exigindo um login e uma chave de acesso (token) antes de mexer nas contas.
* **Criar Contas**: Permite cadastrar novas contas de usuários e ver a lista de contas salvas.
* **Colocar e Tirar Dinheiro (Depósito e Saque)**: O sistema confere tudo direitinho e **não deixa** colocar valores negativos ou zerados.
* **Cuidado com o Saldo**: Se você tentar sacar mais dinheiro do que tem na conta, o sistema bloqueia a operação e avisa que o saldo é insuficiente.
