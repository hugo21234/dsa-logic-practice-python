import enumarado


class SaldoInsuficienteError(Exception):
    """Levantada quando o saque/transferência excede o saldo disponível."""
    pass


class ValorInvalidoError(Exception):
    """Levantada quando o valor informado é zero ou negativo."""
    pass


class ContaBancaria:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.saldo = 0
        self.tipo = tipo

    def depositar(self, valor):
        if valor <= 0:
            raise ValorInvalidoError('Valor deve ser maior que 0')
        self.saldo += valor
        return f'Valor Depositado {valor}'

    def sacar(self, valor):
        if valor <= 0:
            raise ValorInvalidoError('Valor deve ser maior que 0')
        if valor > self.saldo:
            raise SaldoInsuficienteError('Valor maior que o saldo em conta')
        self.saldo -= valor
        return f'Valor Sacado: {valor}'

    def transferir(self, valor, conta):
        c1 = self.numero
        if valor <= 0:
            raise ValorInvalidoError('Valor deve ser maior que 0')
        if valor > self.saldo:
            raise SaldoInsuficienteError('Valor maior que o saldo em conta')
        self.saldo -= valor
        conta.depositar(valor)
        return f'Valor {valor} de {c1} transferido para {conta.numero}'

    def __str__(self):
        return f'Conta {self.numero} | Tipo: {self.tipo.name} | Saldo: R$ {self.saldo}'


# ---- Criando as contas ----
c1 = ContaBancaria(4241, enumarado.Tipo.PESSOA_FISICA)
c2 = ContaBancaria(424, enumarado.Tipo.PESSOA_JURIDICA)

print('--- Contas recém-criadas ---')
print(c1)
print(c2)

print('\n--- Depósitos ---')
try:
    print(c1.depositar(1000))
    print(c2.depositar(500))
except (ValorInvalidoError, SaldoInsuficienteError) as e:
    print(f'Erro no depósito: {e}')
print(c1)
print(c2)

print('\n--- Saques ---')
try:
    print(c1.sacar(200))
except (ValorInvalidoError, SaldoInsuficienteError) as e:
    print(f'Erro no saque: {e}')

try:
    print(c2.sacar(1000))  # deve falhar: saldo insuficiente
except (ValorInvalidoError, SaldoInsuficienteError) as e:
    print(f'Erro no saque: {e}')
print(c1)
print(c2)

print('\n--- Transferência (c1 -> c2) ---')
try:
    print(c1.transferir(300, c2))
except (ValorInvalidoError, SaldoInsuficienteError) as e:
    print(f'Erro na transferência: {e}')
print(c1)
print(c2)

print('\n--- Transferência inválida (valor negativo) ---')
try:
    print(c1.transferir(-50, c2))
except (ValorInvalidoError, SaldoInsuficienteError) as e:
    print(f'Erro na transferência: {e}')
