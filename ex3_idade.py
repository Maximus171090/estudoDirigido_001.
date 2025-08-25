# Condicionais simples com IF, ELIF e ELSE



idade = int(input('Qual a sua idade? '))



if idade >=60:
    print('Você é idoso ')

elif idade >=18:
    print('Você é adulto ')
    

else:
    print("Você é menor de idade")    



#------------------------------------------

idade = int(input('Qual a sua idade? '))


city = input('Qual a sua cidade? ')


if idade >=60:
    print(f'Você é idoso, e mora em {city} ')

elif idade >=18:
    print(f'Você é adulto, e mora em {city} ')
    

else:
    print(f"Você é menor de idade, e mora em {city} ")



    # Fim do script  
