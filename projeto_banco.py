import random

class ContaCorrente:
    def __init__(self, nome_titular, senha):
        self._nome_titular = nome_titular
        self._numero_conta = random.randint(100, 999)
        self._senha = senha
        self._saldo_corrente = 0.0
    
    def get_nome_titular(self):
        return self._nome_titular

    def get_numero_conta(self):
        return self._numero_conta

    def get_saldo_corrente(self):
        return self._saldo_corrente

    def set_saldo_corrente(self, valor):
        self._saldo_corrente = valor

    def verificar_senha(self, senha):
        return self._senha == senha

    def sacar(self, valor, senha):
        if not self.verificar_senha(senha):
            return "Senha incorreta!"
        if valor > self._saldo_corrente:
            return "Saldo insuficiente!"
        self._saldo_corrente -= valor
        return f"Saque de R$ {valor:.2f} realizado com sucesso!"

    def depositar(self, valor):
        if valor < 10:
            return "O depósito mínimo é de R$ 10,00!"
        self._saldo_corrente += valor
        return f"Depósito de R$ {valor:.2f} realizado com sucesso!"

    def aplicar(self, valor, conta_poupanca):
        if valor > self._saldo_corrente:
            return "Saldo insuficiente para a aplicação!"
        self._saldo_corrente -= valor
        conta_poupanca.set_saldo_poupanca(conta_poupanca.get_saldo_poupanca() + valor)
        return f"Aplicação de R$ {valor:.2f} realizada com sucesso!"

class ContaPoupanca(ContaCorrente):
    def __init__(self, nome_titular, senha):
        super().__init__(nome_titular, senha)
        self._saldo_poupanca = 0.0

    def get_saldo_poupanca(self):
        return self._saldo_poupanca

    def set_saldo_poupanca(self, valor):
        self._saldo_poupanca = valor

    def resgatar(self, valor, conta_corrente):
        if valor > self._saldo_poupanca:
            return "Saldo insuficiente para o resgate!"
        self._saldo_poupanca -= valor
        conta_corrente.set_saldo_corrente(conta_corrente.get_saldo_corrente() + valor)
        return f"Resgate de R$ {valor:.2f} realizado com sucesso!"

    def extrato(self):
        return (f"Titular: {self.get_nome_titular()}\n"
                f"Número da conta: {self.get_numero_conta()}\n"
                f"Saldo da Conta Corrente: R$ {self.get_saldo_corrente():.2f}\n"
                f"Saldo da Conta Poupança: R$ {self.get_saldo_poupanca():.2f}")


def main():
    print("Bem-vindo ao Banco!")
    nome_titular = input("Digite o nome completo do titular da conta: ")
    senha = input("Digite uma senha numérica de 4 dígitos: ")
    
    if len(senha) != 4 or not senha.isdigit():
        print("A senha deve ter exatamente 4 dígitos numéricos!")
        return

    conta_corrente = ContaCorrente(nome_titular, senha)
    conta_poupanca = ContaPoupanca(nome_titular, senha)

    
    while True:
        try:
            valor_deposito = float(input("Realize seu primeiro depósito de no mínimo R$ 10,00: "))
            if valor_deposito < 10:
                print("O depósito mínimo é de R$ 10,00!")
            else:
                print(conta_corrente.depositar(valor_deposito))
                print("Conta criada com sucesso!")
                break
        except ValueError:
            print("Por favor, insira um valor numérico válido!")

    
    tentativas = 3
    while tentativas > 0:
        senha_input = input("Digite sua senha para continuar: ")
        if conta_corrente.verificar_senha(senha_input):
            while True:
                print("\nMenu:")
                print("1. Extrato")
                print("2. Sacar")
                print("3. Depositar")
                print("4. Aplicar para poupança")
                print("5. Resgatar da poupança")
                print("6. Sair")
                opcao = input("Escolha uma opção: ")

                if opcao == "1":
                    print(conta_poupanca.extrato())
                elif opcao == "2":
                    valor = float(input("Digite o valor do saque: "))
                    print(conta_corrente.sacar(valor, senha_input))
                elif opcao == "3":
                    valor = float(input("Digite o valor do depósito: "))
                    print(conta_corrente.depositar(valor))
                elif opcao == "4":
                    valor = float(input("Digite o valor para aplicar na poupança: "))
                    print(conta_corrente.aplicar(valor, conta_poupanca))
                elif opcao == "5":
                    valor = float(input("Digite o valor para resgatar da poupança: "))
                    print(conta_poupanca.resgatar(valor, conta_corrente))
                elif opcao == "6":
                    print("Obrigado por usar nosso banco! Até mais.")
                    break
                else:
                    print("Opção inválida!")
        else:
            tentativas -= 1
            if tentativas == 0:
                print("Senha incorreta! Conta bloqueada. Dirija-se à agência com documento de identidade para desbloqueio.")
                break

if __name__ == "__main__":
    main()
