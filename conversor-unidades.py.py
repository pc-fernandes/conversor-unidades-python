'''
Aqui vamos começar os estudos para a criação do conversor. Primeira etapa de foco será no sistema internacional e em temperaturas. Escala de temperaturas em estudo: Celsius, Rankine, Kelvin e Farenheight.

'''

celsius = 1
kelvin = 2
fahrenheit = 3
rankine = 4

print(" Bem vindo ao conversor de temperaturas. \n Marcamos as escalas com números da seguinte forma \n \t\tCelsius = 1 \n \t\tKelvin = 2 \n \t\tFahrenheit = 3 \n \t\tRankine = 4  ")

entrada = int(input ("Digite o número da temperatura de entrada: "))
saida = int(input("Digite o número da temperatura a ser convertida: "))

#temp_entrada = float(input("Qual a temperatura inicial? "))

if entrada == 1 and saida ==2:
  c = float(input("Digite a temperatura em celsius: "))
  k = c + 273.15
  print(f"A temperatura em Kelvin equivale a: {k}")
elif entrada == 2 and saida ==1:
  k = float(input("Digite a temperatura em Kelvin: "))
  c = k - 273.15
  print(f"A temperatura em Celsius equivale a : {c}")
elif entrada == 1 and saida ==3:
  c = float(input("Digite a temperatura em celsius: "))
  f = (c * 1.8) + 32
  print(f"A temperatura em Fahrenheit equivale a: {f} ")
elif entrada == 3 and saida ==1:
  f = float(input("Digite a temperatura em Fahrenheit: "))
  c = (f - 32) / 1.8
  print(f"A temperatura em Celsius equivale a: {c}")
elif entrada == 1 and saida ==4:
  c = float(input("Digite a temperatura em celsius: "))
  r = (c + 273.15) * 1.8
  print(f"A tempertura em Rankine equivale a: {r}")
elif entrada == 4 and saida ==1:
  r = float(input("Digite a temperatura em Rankine: "))
  c = (r / 1.8) - 273.15
  print(f"A temperatura em Celsius equivale a: {c}")
elif entrada == 2 and saida == 3:
  k = float(input("Digite a temperatura em Kelvin: "))
  f = 1.8 * (k - 273.15) + 32
  print(f"A temperatura em Fahrenheit equivale a: {f}")
elif entrada == 3 and saida ==2:
  f = float(input("Digite a temperatura em Fahrenheit: "))
  k = ((f - 32)/1.8)+273.15
  print(f"A temperatura em Kelvin equivale a: {k}")
elif entrada == 2 and saida == 4:
  k = float(input("Digite a temperatura em Kelvin: "))
  r = ((k - 273.15)*1.8)+491.67
  print(f"A temperatura em Rankine equivale a: {r}")
elif entrada == 4 and saida == 2:
  r =  float(input("Digite a temperatura em Rankine: "))
  k = ((r - 491.67) / 1.8) + 273.15
  print(f"A temperatura em Kelvin equivale a: {k}")
elif entrada == 3 and saida == 4:
  f = float(input("Digite a temperatura em Fahrenheit: "))
  r = f + 469.67
  print(f"A temperatura em Rankine equivale a: {r}")
elif entrada == 4 and saida == 3:
  r = float(input("Digite a temperatura em Rankine: "))
  f = r - 469.67
  print(f"A temperatura em Fahrenheit equivale a: {f}")
else: 
  print("Escala não encontrada")
 