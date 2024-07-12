# Verificando se o usuário digitou corretamente.

while True:
    CPF = input('Digite um CPF: ').strip()
    try:
        if len(CPF) == 11:
            break
        else:
            print('Por favor, digite um CPF com 11 números.')
    except:
        print('Digite apenas os números do seu CPF.')
print(f'O CPF digitado foi: {CPF}')

# Primeiro dígito.

lista_cpf = [CPF]
contador = 0
multiplicador = 10
salvar_valor = 0
somatorio = salvar_valor

while True:
    if contador != 9:
        for indice in lista_cpf:            
            numeros = (indice[contador])
            contador += 1            
            resultado = int(numeros) * multiplicador               
            multiplicador -= 1            
            salvar_valor = resultado
            somatorio += salvar_valor            
    else:
        break

multiplicacao = somatorio * 10
resto_divisao_1 = multiplicacao % 11

if resto_divisao_1 > 9:
    digito_01 = (f'0')
else:
    digito_01 = (f'{resto_divisao_1}')

print(f'O primeiro digito é {digito_01}')

# Segundo dígitoo.

lista_cpf = [CPF]
contador = 0
multiplicador = 11
salvar_valor = 0
somatorio = salvar_valor

while True:
    if contador != 10:
        for indice in lista_cpf:            
            numeros = (indice[contador])
            contador += 1            
            resultado = int(numeros) * multiplicador               
            multiplicador -= 1            
            salvar_valor = resultado
            somatorio += salvar_valor            
    else:
        break

multiplicacao = somatorio * 10
resto_divisao_2 = multiplicacao % 11

if resto_divisao_2 > 9:
    digito_02 = (f'0')
else:
    digito_02 = (f'{resto_divisao_2}')
print(f'Seu segundo digito é {digito_02}')

# Validação de CPF

if digito_01 == CPF[9]:
    if digito_02 == CPF[10]:
        print('O CPF é valido.')
    else:
        print('O CPF NÃO é valido!')
else:
    print('O CPF NÃO é valido!')