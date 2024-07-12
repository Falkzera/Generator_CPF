import random
import os

while True:

    escolha = input('Escolha opção [A] ou opção [B]: \n'
    'OPÇÃO [A]: Gerar aleatóriamente o CPF válido.\n'
    'OPÇÃO [B]: Gerar aleatóriamente os primeiros 9 digitos do CPF válido.\n'   
    '[A] ou [B]: '            
    ).strip().upper()

    if escolha.startswith('A'):
        numerador_aleatorio = random.randint(000000000, 999999999)
        gerador_cpf = str(numerador_aleatorio)
        CPF = gerador_cpf
        break

    elif escolha.startswith('B'):
        while True:
            CPF = input('Digite 9 digíto para gerar um CPF Válido: ').strip()
            try:
                if len(CPF) == 9:
                    break
                else:
                    os.system('cls')
                    print('Por favor, digite uma sequência com 9 números.')
            except:
                os.system('cls')
                print('Digite apenas os a sequência de 9 números.')
        os.system('cls')
        print(f'A sequência digitada foi: {CPF}')
        break

    else:
        os.system('cls')
        print('Escolha apenas entre [A ou [B]')
        continue

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
os.system('cls')
print(f'O primeiro digito é {digito_01}')

# Segundo dígitoo.

CPF_1 = str(CPF) + digito_01

lista_cpf = [CPF_1]
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

CPF_2 = str(CPF_1) + digito_02
print(f'O CPF gerado foi: {CPF_2}')

# Testando
if digito_01 == CPF_2[9]:
    if digito_02 == CPF_2[10]:
        print('O CPF é valido.')
    else:
        print('O CPF NÃO é valido!')
else:
    print('O CPF NÃO é valido!')