# While com Parada



senha_correta = "python123"

tentativa = ''

while True:
    tentativa = input('Digite Senha: ')
    if tentativa == senha_correta:
        print('Acesso Permitido! ')
        break
    else:
         print('Acesso Negado! ')

# Colocando número de tentativas





print(input('Pressione Enter para Prosseguir com exercicio de contagem de tentativas nas senhas'))


senha_correta = 'python123'

tentativas_restantes = 3


while tentativas_restantes > 0:
    tentativa = input('Digite a Senha ')
    if tentativa == senha_correta:
        print('✅ Acesso Permitido ')
        break
    else:
        tentativas_restantes -= 1
        print(f'❌ Acesso Negado! Você ainda tem {tentativas_restantes} tentativa(s).')


    if tentativas_restantes == 0:
        print('🚫 Número de tentativas excedido. Acesso bloqueado.')    


