class Produto:
    #__init__ roda automaticamnente quando criamos um objeto novo.
    # "self" é o prorpio objketo sendo criado: é por ele que guardamos os dados.
    def __init__(self, codigo, nome, tipo):
        self.id = codigo#código de barras do produto
        self.nome = nome #nome de identificação do produto
        self.tipo = tipo #"alimenticio", "bzar","limpeza"...

class Lote:
     def __init__(self, codigo, produto, validade, quantidade):
        self.id = codigo
        self.produto = produto
        self.validade = validade
        self.quantidade = quantidade


#Exemplo de produto:
P1 = Produto("35", "creme de leite", "mercearia")
L1 = Lote("215", P1, "17/09/2028", 80)

print (L1.produto.nome, L1.validade)
