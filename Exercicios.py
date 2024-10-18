#EX0.0
valorA = float(input("Insira um valor entre 1 - 20: "))
valorB = float(input("Insira um valor entre 1 - 20: "))
soma = float(valorA + valorB)
media = (soma / 2)
print(media)
-----------------------------------------------------------------------------------------------

#EX0.1
"""
Declara uma variável chamada "idade" e atribuiu a tua idade.
Declara uma variável chamada "nome" e atribuiu o teu nome.
Imprima no ecrã a frase "O meu nome é [nome] e tenho [idade] anos."
"""
idade = input("insira a sua idade: ");
nome = input("Insira o seu nome: ");
print(f"O meu nome é {nome} e tenho {idade} anos.")

-----------------------------------------------------------------------------------------------

#EX0.2
"""
Escreve um programa que imprima "Olá, mundo!" no ecrã.
Cria uma variável chamada "fruta" e atribuiu o nome de uma fruta.
Imprime no ecrã a frase "Eu gosto de [fruta]."
"""
print("Olá Mundo!");
fruta = "Maças";
print(f"Eu gosto de {fruta}.");

-----------------------------------------------------------------------------------------------

#EX0.3
"""
Solicita ao utilizador para digitar o nome.
Imprime no ecrã uma saudação personalizada utilizando o nome fornecido.
Pede ao utilizador para digitar um número inteiro.
Imprime o dobro desse número.
"""
nome = input("Insira o seu nome: ");
print(f"Olá {nome}, tudo bem?");

-----------------------------------------------------------------------------------------------

#EX0.4
"""
Solicita ao utilizador para digitar o nome.
Imprime no ecrã uma saudação personalizada utilizando o nome fornecido.
Pede ao utilizador para digitar um número inteiro.
Imprime o dobro desse número.
"""
nome = input("Qual é o teu nome amigo, diz aí: ");
print(f"Olá {nome}, tudo bem?");
numero = int(input("Insira o número que quer: "));
dobro = numero * 2
print(f"O dobro de {numero} é {dobro}");
print("Tens duvidas, recomeça!");

-----------------------------------------------------------------------------------------------

#EX1.1
"""
Elabora um programa que imprima a mensagem “Bem-vindos ao Python!”, precedida por uma linha em branco
"""
print ("\n Bem-vindo amigo ao Python!")

-----------------------------------------------------------------------------------------------

#EX1.2
"""
Elabora um programa que imprima a mensagem “José, bem-vindo ao Python!”, precedida por uma linha em branco
"""
print (" \n José, bem-vindo ao Python!")

-----------------------------------------------------------------------------------------------

#EX1.3
"""
Elabora um programa que atribua a mensagem a uma variável e, em seguida, imprima o valor da variável.
"""
a= """
Eu gosto da BMW!"""
print(a)

-----------------------------------------------------------------------------------------------

#EX1.4

"""
Elabora um programa que atribua o nome, a idade e a localidade de residência do aluno a três variáveis e imprima os valores dessas variáveis.
"""
nome= input("Como te chamas: ")
idade= int(input ("Quantos anos tem: "))
residencia= input("Onde vives: ")
print(f"O nome do aluno é {nome}, a idade é {idade}, e mora em {residencia}, Dados salvos com sucesso!")

-----------------------------------------------------------------------------------------------

#EX1.5
"""
Elabora um programa que intercale a designação da linguagem de programação e o nome do aluno na mensagem
"""
linguagem= input("Phyton")

-----------------------------------------------------------------------------------------------

#EX1.5
"""
Elabora um programa que intercale a designação da linguagem de programação e o nome do aluno na mensagem
"""
linguagePorg= "Phyton"
nome= input("Qual é o teu nome: ")
print(f"O nome do aluno é {nome} e a linguagem é {linguagePorg}.")

-----------------------------------------------------------------------------------------------

#EX1.6
"""Elabora um programa que alinhe à direita, à esquerda e ao centro a mensagem “Bem-vindo ao Python!” num campo de edição com 50 carateres."""

print(f"{'Bem-vindo ao Python!' :<65}")
print(f"{'Bem-vindo ao Python!' :^65}")
print(f"{'Bem-vindo ao Python!' :>65}")

-----------------------------------------------------------------------------------------------

#EX1.7
"""Elabora um programa que desenvolva o algoritmo de um programa que permita calcular o perímetro e área de uma circunferência a partir do valor do raio."""

raio= float(input("Insira um valor do raio: "))
perimetro= 2 * 3.14 * raio
area= 3.14 * raio * raio
print(f"O valor do perimetro é {perimetro:.2f} e a area é {area: .2f}")

-----------------------------------------------------------------------------------------------

#EX1.8
"""Elabora um programa que imprima a data e horas correntes nos seguintes formatos:
02-10-2024
02-10-2024 16:11:20
10-02-2024 16:11:20
02/10/24
16:11:20"""
import datetime

x = datetime.datetime.now()
dia = x.strftime("%d")
mes= x.strftime("%m")
ano= x.strftime("%y")
print(f"{dia}-{mes}-{ano}")

x = datetime.datetime.now()
dia = x.strftime("%d")
mes= x.strftime("%m")
ano= x.strftime("%y")
horas= x.strftime("%H")
minutos= x.strftime("%m")
segundos= x.strftime("%S")
print(f"{dia}-{mes}-{ano} {horas}-{minutos}-{segundos}")
print(f"{mes}-{dia}-{ano} {horas}-{minutos}-{segundos}")
print(f"{mes}-{dia}-{ano}")
print(f"{dia}/{mes}/{ano}")
print(f"{horas}-{minutos}-{segundos}")

-----------------------------------------------------------------------------------------------

#EX1.9
"""Elabora um programa que leia o número mecanográfico de um atleta, assim como a sua pontuação. O número é inteiro e a pontuação final é real."""
atleta = int(input("Digite o número do atleta: "))
pontos = input("Digite a pontuação final: ")
print(f"O número do atlata é {atleta} e obteve {pontos}.")

-----------------------------------------------------------------------------------------------

#EX1.10
"""Elabora um programa que leia a data de nascimento de uma pessoa e imprima a sua idade à data atual."""

dia = int(input("Insira o dia que nasceu: "))
mes = int(input("insira o mes que nasceu (número do mes): "))
ano = int(input("insira o ano que nasceu: "))
idade = 2024 - ano 
print(f"Na data atual tu tens {idade} anos.")

-----------------------------------------------------------------------------------------------

#EX1.11
"""Elabora um programa que desenvolva o algoritmo de um programa que permita converter libras em euros, considerando a taxa de conversão de 1,19 ( ou seja, 1 GBP = 1,19 EURO)."""

libras = input("Quantidade de libras: ")
euros = 
print(f"Tu em euros tens {euros} euros")

-----------------------------------------------------------------------------------------------

EX N

nome = str(input("Qual é o teu nome? "))
if nome == "Daniel":
  print("Olá administrador da Oficina.")
else:
  print("Olá Utilizador.")
print("Servidor ligado, {}!".format(nome))

-----------------------------------------------------------------------------------------------

import random
segredo= int(random.randint(0,5))
# print(f"o número secreto é {segredo}")
numeroescolhido = int(input("insira um valor entre (0,5): "))
if numeroescolhido != segredo:
  print("O número inserido é maior do que o meu meu!")
elif numeroescolhido < segredo:
  print("O número inserido é menor que o meu!")
else:
  print("Acertaste")

-----------------------------------------------------------------------------------------------

EX-PF

#EX-FP1
"""Verificar se um número é positivo, negativo ou zero.
Escreve um programa em Python que peça ao utilizador para introduzir um número e verifica se ele é positivo, negativo ou igual a zero.
Dica: Usa as estruturas condicionais if, elif e else."""

numero = int(input("Insira um número: "))
if numero > 0:
  print(f"O seu numero é positivo!")
if numero < 0:
  print(f"O seu número é negativo!")
if numero == 0:
  print(f"O seu número é igual!")

-----------------------------------------------------------------------------------------------

#EX-FP2
"""Verificar se um número é par ou ímpar.
Escreve um programa que peça ao utilizador um número inteiro e verifica se ele é par ou ímpar.
Dica: Para verificar se um número é par, utilize a operação de módulo %."""

numero = int(input("Insire um número inteiro ex: 3: "))
if numero % 2 == 0:
  print(f"O seu número é par!")
elif numero % 1 == 0:
  print(f"O seu número é ímpar!")

-----------------------------------------------------------------------------------------------

#EX-FP3
"""Calcular a nota final de um aluno.
Elabora um programa que pergunte ao utilizador a nota final de um aluno e verifica a classificação de acordo com a seguinte tabela:"""

#Nota inferior a 10: "Reprovado"
#Nota entre 10 e 14: "Suficiente"
#Nota entre 15 e 17: "Bom"
#Nota superior a 17: "Muito Bom"


nota = int(input("Qual foi a tua nota final?: "))
if nota < 10:
  print(f"Reprovado")
if nota >= 10 and nota < 15:
  print(f"Suficiente")
if nota >= 15 and nota < 17:
  print(f"Bom")
if nota >= 17:
  print(f"Muito bom")

-----------------------------------------------------------------------------------------------

#EX-FP5

"""Cálculo de impostos
Crie um programa que peça ao utilizador o seu salário mensal e calcule o imposto de acordo com a seguinte tabela:

Salário até 1000: isento de impostos
Salário entre 1001 e 2000: 10% de imposto
Salário superior a 2000: 20% de imposto
O programa deve exibir o salário após a dedução do imposto."""

salario = int(input("Qual é o seu salario mensal?: "))

----------------------------------------------------------------------------------------------

#EX-FP4

"""Conversor de temperaturas.
Cria um programa que pergunte ao utilizador uma temperatura em graus Celsius e a converta para Fahrenheit, Kelvin ou ambas. O utilizador deve escolher a unidade de destino (Fahrenheit ou Kelvin), e o programa deve exibir o valor convertido.

Fórmulas:

Fahrenheit = Celsius * 9/5 + 32
Kelvin = Celsius + 273.15"""

print(f"{'Convertor de Temperatura TERMINAL' :^65}")
Celsius = float(input("Insira a temperatura em graus Celsius: "))

Fahrenheit = (Celsius * 9/5) + 32
Kelvin = Celsius + 273.15

opcao = str(input("Escolha a conversão oara Fahrenheit (F), kelvin (K) ou Ambas (A): "))
if opcao == "F":
  print (f"O valor em fahrenheirt é {Fahrenheit}")
elif opcao == "K":
  print (f"O valor em Kelvin é {Kelvin}")
elif opcao == "A":
  print (f"O valor em Fahreneheit é {Fahrenheit} e em Kelvin é {Kelvin}.")
else:
  print ("Opção inválida ")

-----------------------------------------------------------------------------------------------

"""Cálculo de impostos
Crie um programa que peça ao utilizador o seu salário mensal e calcule o imposto de acordo com a seguinte tabela:

Salário até 1000: isento de impostos
Salário entre 1001 e 2000: 10% de imposto
Salário superior a 2000: 20% de imposto
O programa deve exibir o salário após a dedução do imposto."""
#FP5
salario = float(input("Insira o seu salário mensal: "))
if salario <= 1000:
  print("O seu imposto é 0 está isento de imposto")
elif salario > 1000 and salario < 2000:

  imposto = salario * 0.10
  salarioImposto = salario - imposto
  print(f"O seu salário mensal com o imposto de 10% é de: {salarioImposto}")
elif salario >= 2000:
  salarioImposto = salario * 0.20
  print(f"O seu salário mensal com o imposto de 20% é de: {salarioImposto:.2f}€")

-----------------------------------------------------------------------------------------------------------------------

#E FP6
"""Imprimir números de 1 a 10.
Escreve um programa em Python que use um ciclo for para imprimir todos os números de 1 a 10."""

for x in range(1,11):
  print(x)

--------------------------------------------------------------------------------------------------------------------------

#E FP7
"""Soma de números de 1 a 100.
Escreve um programa que use um ciclo while para calcular a soma de todos os números de 1 a 100."""

r = 1
soma = 0

while r <= 100:
  soma = soma + r
  r = r + 1
print(f"A soma dos números de 1 a 100 é: {soma}")

--------------------------------------------------------------------------------------------------------------------------

#E FP8
"""Contagem de vogais numa string.
Escreve um programa que peça ao utilizador para introduzir uma frase e utilize um ciclo for para contar quantas vogais (a, e, i, o, u) existem na frase."""

frase = input("Insira uma frase: ")
vogais = 0
for letra in frase:
    if letra in "aeiouAEIOU":
      vogais = vogais + 1
print(f"A frase tem {vogais} vogais")

--------------------------------------------------------------------------------------------------------------------------

#EXFP9
"""
Escreve um programa que utilize um ciclo for para listar todos os múltiplos de 5 entre 1 e 50.
"""
for i in range(1,51):
  if i%5==0:
    print(i)

--------------------------------------------------------------------------------------------------------------------------

#E FP10: Verificar se um número é primo.
"""Escreve um programa que crie uma lista de 5 números inteiros, pede ao utilizador para introduzir cada número e, em seguida, calcula e exibe a média desses números."""

notas = []
for i in range(1,6):
  num = int(input(f"escreva um número inteiro: "))
  notas.append(num) #Adicionar um elemento á lista.
soma = sum(notas) #calcula a soma de todos os elementos dentro da lista.
x = len(notas) #devolve o número total de elementos da lista.
media = (soma / x)
print(media)

---------------------------------------------------------------------------------------------------------------------------

#E FP11: Verificar se um número é primo.
"""Escreve um programa que peça ao utilizador um número inteiro e verifique se ele é primo. Um número primo é divisível apenas por 1 e por ele mesmo. O programa deve utilizar um ciclo for para testar se o número é divisível por algum outro número."""

numero = int(input("número: "))
divisores = 0
for i in range(1, numero + 1):
  if numero % i == 0:
    divisores += 1
if divisores == 2:
  print(f"o {numero} é um numero primo")
else:
  print(f"o {numero} não é numero primo")

---------------------------------------------------------------------------------------------------------------------------

#Exercício FP12: Gerar uma lista de números pares.
"""Cria um programa que utilize a função range() e um ciclo for para gerar uma lista com todos os números pares entre 1 e 20 e imprima a lista."""

lista = []
for i in range(1,21):
  if i % 2 == 0:
    lista.append(i)
print(f"Os números pares: {lista}")

---------------------------------------------------------------------------------------------------------------------------

#Exercício FP13: Inverter uma string.
"""Escreve um programa que peça ao utilizador para introduzir uma palavra ou frase e utilize um ciclo para imprimir a string invertida."""

texto = str(input("Insira um texto: ")) #Pedir o texto ao utilizador
textoinv = texto[::-1] #Script para inverter o texto
print(textoinv) #Printar o texto invertido

---------------------------------------------------------------------------------------------------------------------------

#Exercício FP14: Tabuada de multiplicação
"""Escreve um programa que gere a tabuada de multiplicação de um número introduzido pelo utilizador. O programa deve utilizar um ciclo for para calcular e exibir a tabuada até 10."""

num = int(input("Insira um numero: "))
for i in range(1,11):
  resultado = num * i
  print(f"{num} x {i} = {resultado}")

---------------------------------------------------------------------------------------------------------------------------

#Exercício FP15: Fatorial de um número
"""Escreve um programa que utilize um ciclo while para calcular o fatorial de um número introduzido pelo utilizador. O fatorial de um número n (n!) é o produto de todos os números inteiros positivos até n."""

int(input("insira um numero:"))
fatorial = 1
i = 1
while i <= fatorial:
  fatorial = i
  i+= 119
  print(i)
