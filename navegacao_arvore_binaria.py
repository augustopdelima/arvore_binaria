class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


def percorrer_arvore(raiz: No, nivel, resultado: list):

    if raiz is None:
        return

    if len(resultado) <= nivel:
        resultado.append([])

    resultado[nivel].append(raiz.valor)

    percorrer_arvore(raiz.direita, nivel+1, resultado)
    percorrer_arvore(raiz.esquerda, nivel+1, resultado)

    return resultado


raiz = No(3)
segundo_no = No(9)
terceiro_no = No(20)
quarto_no = No(15)
quinto_no = No(7)

raiz.esquerda = segundo_no
raiz.direita = terceiro_no

terceiro_no.direita = quarto_no
terceiro_no.esquerda = quinto_no


print(percorrer_arvore(raiz, 0, []))
