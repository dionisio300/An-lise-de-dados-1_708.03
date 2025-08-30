# Listas
# nomes = ['Maria','João','Pedro','Carlos']
# nome = input('Digite o nome: ')

# append - Adiciona um elemento no final de uma lista
# nomes.append(nome)
# print(nomes)

# pop - Remove um elemento do final da lista
# nomes.pop(0)
# print(nomes)

# nomes.remove('João')
# print(nomes)

# # Dicionários

# pessoa1 = {
#     "Nome":'Maria',
#     "idade":28
# }
# print(pessoa1['Nome'])

# dadosPessoa = {}

# dadosPessoa['Nome'] = input('Digite seu nome: ')
# dadosPessoa['idade'] = int(input('Digite sua idade: '))
# dadosPessoa['CPF'] = input('Digite seu CPF: ')
# dadosPessoa['CEP'] = input('Digite seu CEP: ')

# print(dadosPessoa)

# nome = input('Digite seu nome')
# idade = input('Digite sua idade')
# cep = input('Digite seu cep')
# cpf = input('Digite seu cpf')

# dadosPessoa2 = {
#     'nome':nome,
#     'idade':int(idade),
#     'cep':cep,
#     'cpf':cpf
# }
# print(dadosPessoa2)

# pessoa2 = {
#     "Nome":'João',
#     "idade":30
# }
# print(pessoa2['Nome'])
# pessoas = []
# pessoas.append(pessoa1)
# pessoas.append(pessoa2)
# print(pessoas)


cadastroPessoas = []
while True:
    print('1 - Cadastrar\n2 - Buscar\n3 - Sair')
    opcao = int(input())
    if opcao == 3:
        break
    elif opcao == 1:
        nome = input('Nome: ')
        idade = int(input('idade: '))
        cpf = input('CPF: ')
        cep = input('CEP: ')
        cadastro = {'nome':nome,'idade':idade,'cpf':cpf,'cep':cep}
        cadastroPessoas.append(cadastro)
        print('Cadastro Realizado com sucesso!!')
    elif opcao == 2:
        nomeBuscado = input('Nome: ')
        for pessoa in cadastroPessoas:
            if pessoa['nome'] == nomeBuscado:
                print(f'Nome: {pessoa['nome']}')
                print(f'Idade: {pessoa['idade']}')
                print(f'CPF: {pessoa['cpf']}')
                print(f'CEP: {pessoa['cep']}')  
            print('Pessoa não encontrada')

# Funções

# def nomeDaFuncao(Parâmetros):

#     print('Corpo da função')

#     return

# def soma(a,b):
#     print(a+b)

# Funções sem parâmetro e sem retorno

def mensagemDeErro():
    print('Erro ao tentar executar a operação')

# Função sem parâmetro e com retorno

def mensagemDeErro2():
    return 'Erro ao tentar executar a operação 2'

# Funções com parâmetro e sem retorno

def saudacao(nome:str, idade:int):
    print(f'Olá {nome}, você tem {idade} anos de idade!')

# Função com parâmetro e com retorno 

def saudacao2(nome,idade):
    saudacao = f'Olá {nome}, você tem {idade} anos de idade, Função 2'
    return saudacao

def subtracao(a,b):
    return a - b

# Função com parâmetros não obrigatórios
def saudacao3(nome = 'fulano',idade = 100):
    saudacao = f'Olá {nome}, você tem {idade} anos de idade, Função 2'
    return saudacao



print(saudacao3())


mensagemDeErro()

erro = mensagemDeErro2()

print(f'{erro} acesso ao banco de dados')

saudacao('João',20)

print(saudacao2('João',20))


print(subtracao(10,2))

print(subtracao(b = 2,a = 10))



