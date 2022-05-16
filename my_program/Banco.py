class Conta:
    def __init__(self, nome, agencia, conta, cpf):
        self.nome = nome
        self.agencia = agencia
        self.conta = conta
        self.cpf = cpf
        self.saldo = 0

class Transferencia:
    def __init__(self, id, valor, tipo):
        self.id = int(id)
        self.valor = float(valor)
        self.tipo = tipo
    
    def valida_tipo(self):
        if self.id == 1 and self.tipo != 'PIX':
            print("Erro: ID e tipo de transferência não correspondem")
            print("ID = 1, esperado PIX, recebido ", self.tipo)
            return False
        elif self.id == 2 and self.tipo != 'TED':
            print("Erro: ID e tipo de transferência não correspondem")
            print("ID = 2, esperado TED, recebido ", self.tipo)
            return False
        elif self.id == 3 and self.tipo != 'DOC':
            print("Erro: ID e tipo de transferência não correspondem")
            print("ID = 3, esperado DOC, recebido ", self.tipo)
            return False
        return True

    def valida_valor(self):
        if self.id == 1 and self.valor > 5000:
            print("PIX não é um método válido para valores acima de R$5.000,00.")
            return False
        elif self.id == 2 and self.valor < 5000 or self.valor > 10000:
            print("TED não é um método válido para valores abaixo de R$ 5.000,00 ou acima de R$ 10.000,00.")
            return False
        elif self.id == 3 and self.valor < 10000:
            print("DOC não é um método válido para valores abaixo de R$10.000,00.")
            return False
        elif self.valor <= 0:
            print("Valor de transferência inválido. Insira um valor acima de zero.")
            return False
        return True

try:
    arquivo = open('entrada.txt', 'r')
    conteudo = arquivo.readlines()[2].rstrip()
except:
    print("ERRO: Arquivo inválido.")
    exit()
l_conteudo = list(conteudo.split('|'))
if len(l_conteudo) != 11:
    print("ERRO: Entrada inválida")
    print("Valores esperados: 11")
    print("Valores recebidos: ", len(l_conteudo))
    exit()

emissor = Conta(l_conteudo[3], l_conteudo[4], l_conteudo[5], l_conteudo[6])
receptor = Conta(l_conteudo[7], l_conteudo[8], l_conteudo[9], l_conteudo[10])
transferencia = Transferencia(l_conteudo[0], l_conteudo[1], l_conteudo[2])

if emissor.conta == receptor.conta:
    print("Não é possível realizar uma transferência para a própria conta.")
    exit()
if transferencia.valida_tipo():
    if (transferencia.valida_valor()):
        emissor.saldo -= transferencia.valor
        receptor.saldo += transferencia.valor
        print("Transferência realizada com sucesso.")
        print("Saldo do emissor: R$ ", emissor.saldo)
        print("Saldo do receptor: R$ ", receptor.saldo)