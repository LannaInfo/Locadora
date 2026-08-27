jogos = []


def cadastro_jogo(titulo,plataforma,genero,locacao_dia):

    jogo = {
        'titulo': titulo,
        'plataforma': plataforma,
        'genero': genero,
        'locacao_dia': locacao_dia
    }
    jogos.append(jogo)
    return jogo


def listar_jogo(jogos):
    if  not  jogos:
        print('--- Lista vazia ---')
        return
    
    for jogo in jogos:
        print(f'\nTitulo: {jogo['titulo']}')
        print(f'\nPlataforma: {jogo['plataforma']}')
        print(f'\ngenero: {jogo['genero']}')
        print(f'\nValor: {jogo['Valor']}')
        
