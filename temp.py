def formatar_moeda(valor_antigo):
    valor = valor_antigo.replace("R$", "").strip()

    if valor.isnumeric():
        if "-" in valor:
            valor = valor.replace("-", "")
        if "," in valor:
            valor = float(valor.replace(",", ""))
        if "." in valor:
            valor = valor.replace(".", "")
        if len(valor) == 1:
            numponto = "00" + valor
        elif len(valor) == 2:
            numponto = "0" + valor
        elif 6 <= len(valor) <= 8:
            numponto = valor[:-5] + "." + valor[-5:]
        elif 9 <= len(valor) <= 11:
            numponto = inserir_ponto(8, valor)
        elif 12 <= len(valor) <= 14:
            numponto = inserir_ponto(11, valor)
        else:
            numponto = valor
        numvirgula = numponto[:-2] + "," + numponto[-2:]
        return "R$ " + numvirgula
    return valor_antigo


def inserir_ponto(pos, valor):
    return valor[:pos] + "." + valor[pos:]
