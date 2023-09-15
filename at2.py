#DIA 17/08
#1. Faça um algoritmo que leia um número N, some todos os números inteiros de 1 a N, e mostre o resultado obtido.
n = int(input("Digite um número inteiro: "))
soma = 0

for i in range(1, n + 1):
    soma += i

print("A soma dos números de 1 a n é:",soma)

#2. A série de Fibonacci é formada pela seguinte seqüência: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#etc. Escreva um algoritmo que gere a série de Fibonacci até o vigésimo termo.
termo_anterior = 1
termo_atual = 1

print(termo_anterior)
print(termo_atual)

for _ in range(18):
    proximo_termo = termo_anterior + termo_atual
    print(proximo_termo)

    termo_anterior = termo_atual
    termo_atual = proximo_termo

#3 Escreva um algoritmo que leia um conjunto de 20 números inteiros e mostre qual foi o
#maior e o menor valor fornecido.
maior = float('-inf')
menor = float('inf')

for _ in range(20):
    numero = int(input("Digite um número inteiro: "))

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print("O menor valor fornecido é: ",menor)
print("O maior valor fornecido é: ",maior)

#4 Imprima uma tabela de conversão de polegadas para centímetros, de 1 a 20. Considere
#que Polegada = Centímetro * 2,54.
def polegada_para_cm(polegadas):
    return polegadas * 2.54

print("Polegadas\Centímetros")

for polegadas in range(1, 21):
    centimetros = polegada_para_cm(polegadas)
    print(f"{polegadas}\t\t{centimetros:.2f}")

#5 Crie um algoritmo que receba do usuário um número qualquer e verifique se esse é múltiplo de 5.
numero = int(input("Digite um número: "))

if numero % 5 == 0:
    print(f"{numero} é um múltiplo de 5.")
else:
    print(numero, "não é um múltiplo de 5.")

#6 Leia a velocidade máxima permitida em uma avenida e a velocidade com que o motorista estava dirigindo nela. Calcule e mostre a multa que uma pessoa vai receber,sabendo que são pagos: R 50reaisseomotoristaultrapassarematé10km/havelocidadepermitida;R  100 reais, se o motorista ultrapassar de 11 a 30 km/h a velocidade permitida; e R$ 200 reais, se estiver acima de 31km/h da velocidade permitida.
def calcular_multa(velocidade_maxima, velocidade_motorista):
    limite_10 = velocidade_maxima + 10
    limite_30 = velocidade_maxima + 30

    if velocidade_motorista <= limite_10:
        multa = 50
    elif velocidade_motorista <= limite_30:
        multa = 100
    else:
        multa = 200

    return multa

velocidade_maxima = int(input("Digite a velocidade máxima permitida (em km/h): "))
velocidade_motorista = int(input("Digite a velocidade do motorista (em km/h): "))

multa = calcular_multa(velocidade_maxima, velocidade_motorista)
print("A multa a ser paga é de R$", multa)

#7 Escreva um algoritmo que leia dois números e apresente um menu de opções como o
#mostrado abaixo: a. Leia a opção do usuário e execute a operação com os dois números lidos anteriormente.
def soma(a, b):
    return a + b

def diferenca(a, b):
    return abs(a - b)

def produto(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida"

print("Digite dois números:")
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))

print("Escolha a opção:")
print("1 - Soma de 2 números.")
print("2 - Diferença entre 2 números (maior pelo menor).")
print("3 - Produto entre 2 números.")
print("4 - Divisão entre 2 números (o denominador não pode ser zero).")

opcao = int(input("Opção: "))

if opcao == 1:
    resultado = soma(num1, num2)
elif opcao == 2:
    resultado = diferenca(max(num1, num2), min(num1, num2))
elif opcao == 3:
    resultado = produto(num1, num2)
elif opcao == 4:
    resultado = divisao(num1, num2)
else:
    resultado = "Opção inválida"

print("Resultado:", resultado)

#8 Crie um algoritmo que, dada uma temperatura em graus célsius, exiba uma mensagem
#informando o tipo do clima, de acordo com as seguintes condições: se a temperatura estiver até 18 graus, o clima é frio; se a temperatura estiver entre 19 e 23 graus, o clima é agradável; se a temperatura estiver entre 24 e 35 graus, o clima é quente; se a temperatura estiver acima de 35 graus, o clima é muito quente.
temperatura = float(input("Digite a temperatura em graus Celsius: "))

if temperatura <= 18:
    clima = "frio"
elif temperatura <= 23:
    clima = "agradável"
elif temperatura <= 35:
    clima = "quente"
else:
    clima = "muito quente"

print("O clima é", clima)


#DIA 31/08
#1 Receba uma string informada pelo usuário e exiba cada caractere informado em uma linha diferente.
palavra = input("Digite alguma palavra:")
print(palavra.replace("", "\n"))

#2 E-mail: vamos validar um padrão de e-mail informado pelo usuário
#A. Deve conter um caractere @
#B. O @ não pode ser o primeiro caractere
#C. O @ Não pode ser o último caractere (Dica função len retorna o tamanho de uma string)
#D. Deve terminar com .com
#C. Conter no mínimo 10 caracteres.

import re

def validar_email(email):

    if '@' not in email:
        return False

    if email.index('@') == 0:
        return False

    if email.index('@') == len(email) - 1:
        return False

    if not email.endswith('.com'):
        return False

    if len(email) < 10:
        return False

    return True

email = input("Digite um endereço de e-mail: ")

if validar_email(email):
    print("O e-mail é válido.")
else:
    print("O e-mail é inválido.")