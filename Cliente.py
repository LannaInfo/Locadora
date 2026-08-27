
clientes = []
def cadastrar_cliente(nome,telefone):
    cliente = {
        'nome': nome,
        'telefone': telefone
    }
    clientes.append(cliente)
    return cliente

def listar_cliente(clientes):
    if  not  clientes:
        print('--- Lista vazia ---')
        return
    
    for cliente in clientes:
        print(f'\nnome: {cliente['nome']}')
        print(f'\ntelefone: {cliente['telefone']}')
    
        
