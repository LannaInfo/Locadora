import json

def salvar_jogos(jogos):
    with open("jogo.json", "w", encoding="utf-8") as arquivo:
       json.dump(jogos, arquivo, indent=4) 

def carregar_jogo():
    try:
        with open("jogo.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
            return []