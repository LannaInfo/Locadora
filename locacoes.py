from Persistencia import salvar_jogos


def calcular_desconto(dias, valor_diaria):
    valor_total = dias * valor_diaria

    if dias > 7:
        percentual_desconto = 10
    elif dias > 3:
        percentual_desconto = 5
    else:
        percentual_desconto = 0

    valor_desconto = valor_total * (percentual_desconto / 100)
    valor_final = valor_total - valor_desconto

    return valor_total, percentual_desconto, valor_desconto, valor_final


def realizar_locacao(locacoes, cliente, jogo, dias):
    valor_total, percentual_desconto, valor_desconto, valor_final = calcular_desconto(
        dias,
        jogo["locacao_dia"]
    )

    locacao = {
        "cliente": cliente["nome"],
        "telefone": cliente["telefone"],
        "jogo": jogo["titulo"],
        "plataforma": jogo["plataforma"],
        "dias": dias,
        "valor_diaria": jogo["locacao_dia"],
        "valor_total": valor_total,
        "desconto": percentual_desconto,
        "valor_desconto": valor_desconto,
        "valor_final": valor_final
    }

    locacoes.append(locacao)

    salvar_dados("locacoes.json", locacoes)

    return locacao


def listar_locacoes(locacoes):
    if not locacoes:
        print("\n--- Nenhuma locação realizada. ---")
        return

    print("\n========== LOCAÇÕES REALIZADAS ==========")

    for indice, locacao in enumerate(locacoes, start=1):
        print(f"\nLocação {indice}")
        print(f"Cliente: {locacao['cliente']}")
        print(f"Telefone: {locacao['telefone']}")
        print(f"Jogo: {locacao['jogo']}")
        print(f"Plataforma: {locacao['plataforma']}")
        print(f"Dias: {locacao['dias']}")
        print(f"Valor da diária: R$ {locacao['valor_diaria']:.2f}")
        print(f"Valor total: R$ {locacao['valor_total']:.2f}")
        print(f"Desconto: {locacao['desconto']}%")
        print(f"Valor do desconto: R$ {locacao['valor_desconto']:.2f}")
        print(f"Valor final: R$ {locacao['valor_final']:.2f}")

    print("\n=========================================")
