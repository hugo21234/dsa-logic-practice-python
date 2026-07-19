# 💸 Mini Projeto: Conta Bancária em Python (POO)

Este projeto é uma simulação simples de uma **conta bancária** implementada em
Python usando **Programação Orientada a Objetos (POO)**.

O foco não é interface gráfica nem banco de dados, mas sim:
- Modelar uma conta como um **objeto** com estado e comportamento.
- Aplicar **regras de negócio** (depósito, saque, transferência) de forma segura.
- Usar **exceções customizadas** para representar erros de domínio.

---

## 🧩 Objetivo do projeto

Treinar conceitos fundamentais de POO em Python:

- **Classes e objetos** (`ContaBancaria`).
- **Encapsulamento** de estado (`saldo`, `numero`, `tipo`).
- **Métodos de instância** (`depositar`, `sacar`, `transferir`).
- **Validação de regras de negócio** com exceções (`SaldoInsuficienteError`, `ValorInvalidoError`).
- Integração com **Enum** para o tipo da conta (Pessoa Física / Pessoa Jurídica).

Este projeto é um degrau inicial para sistemas bancários mais completos
(clientes, múltiplas contas, histórico de transações, persistência em banco etc.).

---

## 🏗 Estrutura do código

O código principal está em um arquivo único (`conta_bancaria.py`) e contém:

- `SaldoInsuficienteError`  
  Exceção lançada quando o saque ou a transferência excedem o saldo disponível.

- `ValorInvalidoError`  
  Exceção lançada quando o valor informado é zero ou negativo.

- `ContaBancaria`  
  Classe que representa uma conta bancária básica:
  - `numero`: identificador da conta.
  - `tipo`: tipo da conta (enum: Pessoa Física / Pessoa Jurídica).
  - `saldo`: valor atual em conta (inicia em zero).

  Métodos principais:
  - `depositar(valor)` — valida `valor > 0`, atualiza saldo.
  - `sacar(valor)` — valida `valor > 0` e `valor <= saldo`, atualiza saldo.
  - `transferir(valor, conta_destino)` — valida, debita origem, credita destino via `depositar`.
  - `__str__` — representação amigável: `Conta <numero> | Tipo: <tipo.name> | Saldo: R$ <saldo>`.

---

## ▶️ Como executar

1. Clone o repositório.
2. Confirme que `enumarado.py` está no mesmo diretório (define o Enum `Tipo`).
3. Execute:

```bash
python conta_bancaria.py
```

---

## 🧪 Comportamento esperado

- Contas recém-criadas com saldo inicial zero.
- Depósitos válidos atualizando o saldo.
- Tentativa de saque acima do saldo → `SaldoInsuficienteError`.
- Transferência válida atualizando saldos de origem e destino.
- Transferência com valor negativo → `ValorInvalidoError`.

Erros tratados com `try/except`, exibindo mensagens amigáveis.

---

## 🔮 Próximos passos

- Adicionar classe `Cliente` vinculada a cada conta.
- Implementar histórico de transações.
- Persistir em banco de dados (PostgreSQL).
- Garantir atomicidade de transferências com transações ACID.
- Expor via API (FastAPI).

---

## 📚 Conceitos praticados

- Programação Orientada a Objetos em Python.
- Modelagem de domínio simples (Conta Bancária).
- Enum como conjunto de constantes nomeadas.
- Exceções customizadas para regras de negócio.
- Separação entre lógica de domínio e interface de texto.
