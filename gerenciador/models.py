class Produto:
    # __init__ roda automaticamnente quando criamos um objeto novo.
    # "self" é o prorpio objketo sendo criado: é por ele que guardamos os dados.
    def __init__(self, codigo, nome, setor):
        self.id = codigo  # código de barras do produto
        self.nome = nome  # nome de identificação do produto
        self.setor = setor  # "alimenticio", "bazar","limpeza"...


class Lote:
    def __init__(self, codigo, produto, date, carga_atual):
        self.id = codigo
        self.produto = produto
        self.date = date
        self.carga_atual = carga_atual

    def descarregar(self, caixas):
        if self.carga_atual < caixas:
            return False #Return devolve uma resposta a quem chamou o método
        if caixas <= 0:
            return False
        self.carga_atual = self.carga_atual - caixas
        return True


# Exemplo de produto:
P1 = Produto("35", "creme de leite", "mercearia")
L1 = Lote("215", P1, "17/09/2028", 80)

print(L1.descarregar(90))
print(L1.descarregar(-30))
print(L1.carga_atual)