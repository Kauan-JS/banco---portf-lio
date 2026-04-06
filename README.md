# banco---portfolio

SISTEMA DE CONTA BANCÁRIA EM PYTHON

Descrição:
Este projeto simula uma conta bancária simples em Python, permitindo realizar depósitos, saques e visualizar o saldo da conta.

Funcionalidades:

* Criar uma conta bancária
* Depositar dinheiro
* Sacar dinheiro (com verificação de saldo)
* Exibir informações da conta

Classe:
ContaBancaria

Atributos:

* ID: número da conta
* Titular: nome do dono da conta
* saldon: saldo atual

Métodos:

* Deposito(valor): adiciona valor ao saldo
* Saque(valor): realiza saque se houver saldo suficiente
* **str**(): retorna os dados da conta

Exemplo de uso:

hamaki = ContaBancaria(610562, 'Hamaki', 5000)

hamaki.Deposito(100)
hamaki.Saque(5200)
hamaki.Saque(500)

print(hamaki)

Saída esperada:
Saque de R$5200 NEGADO! SALDO INSUFICIENTE!
A conta 610562 de Hamaki tem o saldo de R$4600.00

Observações:

* Não há validação para valores negativos
* Os dados não são salvos (sem banco de dados)
* O sistema é apenas para fins de aprendizado

Possíveis melhorias:

* Validar valores negativos
* Criar múltiplas contas
* Adicionar interface gráfica
* Salvar dados em arquivo
