# Funções 

def saudacao(nome):
    return f'Olá, {nome}!'

def idade_para_100(idade):
    if idade >= 100:
        return 'Ual! você tem mais de 100 anos!'
    else:
        return f'Faltam {100 - idade} anos para você completar 100'

usuario = input("Digite seu nome: ")
idade = int(input("Qual a sua idade? "))  # <- Aqui está a correção

print(saudacao(usuario))
print(idade_para_100(idade))