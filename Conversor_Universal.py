import requests
import json
import os
import sys
import time
from prettytable import *


#____Consumo___da__API#
url= requests.get("https://economia.awesomeapi.com.br/json/all")
cotacao = url.json()
names =  list(cotacao)
#____Consumo___da__API#




#___Fatiamento/Organizacao__dos_dados___#
moedas_usuais = [ names[0],names[2], names[7], names[8]]
criptomoedas = [ names[5],names[6],names[13],names[15]]
moedas_exo =[names[1],names[3],names[4], names[9],names[10], names[11],names[12],names[14]]
#___Fatiamento/Organizacao__dos_dados___#





#__________ACUMULADORES________#
conversoes = {}
response = []
moeda_str = [ ]
#__________ACUMULADORES________#




def menu_comum():
	print("\033[1m...\033[m"*34,"\n")
	print(("""
				●  MOEDAS COMUNS  ●
	
			|	\033[1;36m[ \033[m1\033[1;36m ]\033[m -  USD		|
			|	\033[1;36m[ \033[m2\033[1;36m ]\033[m -  CAD		|
			|	\033[1;36m[ \033[m3\033[1;36m ]\033[m -  EUR		|
			|	\033[1;36m[ \033[m4\033[1;36m ]\033[m -  JPY		|

"""))
	print("\033[1m...\033[m"*34,"\n")
	cont = 0
	tent = 0
	while True:
		cont += 1
		try:
			print("\n")
			opc = int(input("  ◇   Escolha uma moeda :  "))
			if opc == 1 or opc == 2 or opc == 3 or opc == 4:
				print("\n")
				moeda = float(input("  •  Seu Dinheiro [ BRL ] : "))
				cambio = float(cotacao[f"{moedas_usuais[opc-1]}"]["bid"])
				convert = moeda * cambio
				print("\n")
				print(f"  ◇  Dinheiro : R${moeda:.2f}   //   Convertido[{moedas_usuais[opc-1]}] : {convert:.2f}")
				print("\n")
				p  = " "
				r = str(opc)
				name_coin = r.replace(f"{r}", f"{moedas_usuais[opc-1]}")
				conversoes["BRL"] = moeda
				conversoes[f"{name_coin}"] = name_coin
				conversoes["Conversão"] = f"{convert:.3f}"
				final = conversoes.copy()
				response.append(final)
				moeda_str.append(conversoes[f"{name_coin}"])
				conversoes.clear()
				while p not in "SN":
					p = str(input("  ■  Deseja Voltar ao Menu Inicial [ S / N ] ? :")).upper()
					if p in "S":
						os.system("clear")
						inicio()
					elif p in "N":
						os.system("clear")
						menu_comum()
			if opc > 4 or opc < 1:
				tent += 1
				print(f"\033[1;31m  •  Escolha inválida : {opc} inexistente no sistema  \033[m")
			if tent == 3:
				os.system("clear")
				menu_comum()
				tent = 0
		except ValueError as erro:
			tent += 1
			print(f"\033[1;31m  •  Escolha inválida.  \033[m")
			if tent == 3:
				os.system("clear")
				menu_comum()
				tent = 0


	
def menu_exo():
	print("\033[1m...\033[m"*34,"\n")
	print(("""				●  MOEDAS EXÓTICAS  ●
					
			|	\033[1;36m[ \033[m1\033[1;36m ]\033[m -  USDT		|
			|	\033[1;36m[ \033[m2\033[1;36m ]\033[m -  GBP		|
			|	\033[1;36m[ \033[m3\033[1;36m ]\033[m -  ARS		|
			|	\033[1;36m[ \033[m4\033[1;36m ]\033[m -  CHF		|
			|	\033[1;36m[ \033[m5\033[1;36m ]\033[m -  AUD		|
			|	\033[1;36m[ \033[m6\033[1;36m ]\033[m -  CNY		|
			|	\033[1;36m[ \033[m7\033[1;36m ]\033[m -  ILS		|
			|	\033[1;36m[ \033[m8\033[1;36m ]\033[m -  XRP		|
"""))
	print("\033[1m...\033[m"*34,"\n")
	tent = 0
	while True:
		try:
			print("\n")
			opc = int(input("  ◇   Escolha uma moeda :  "))
			if opc == 1 or opc == 2 or opc == 3 or opc == 4 or opc == 5 or opc == 6 or opc == 7 or opc == 8:
				print("\n")
				moeda = float(input("  •  Seu Dinheiro [ BRL ] : "))
				cambio = float(cotacao[f"{moedas_exo[opc-1]}"]["bid"])
				convert = moeda * cambio
				print("\n")
				print(f"  ◇  Dinheiro : R${moeda:.2f}   //   Convertido[{moedas_exo[opc-1]}] : {convert:.2f}")
				print("\n")
				p  = " "
				r = str(opc)
				name_coin = r.replace(f"{r}", f"{moedas_exo[opc-1]}")
				conversoes["BRL"] = moeda
				conversoes[f"{name_coin}"] = name_coin
				conversoes["Conversão"] = f"{convert:.3f}"
				final = conversoes.copy()
				response.append(final)
				moeda_str.append(conversoes[f"{name_coin}"])
				conversoes.clear()
				while p not in "SN":
					p = str(input("  ■  Deseja Voltar ao Menu Inicial [ S / N ] ? :")).upper()
					if p in "S":
						os.system("clear")
						inicio()
						return names
					elif p in "N":
						os.system("clear")
						menu_exo()
					
			if opc > 8 or opc < 1:
				tent += 1
				print(f"\033[1;31m  •  Escolha inválida : {opc} inexistente no sistema.  \033[m")
			if tent == 3:
				os.system("clear")
				menu_exo()
				tent = 0
		except ValueError as erro:
			tent += 1
			print(f"\033[1;31m  •  Escolha inválida.  \033[m")
			if tent == 3:
				os.system("clear")
				menu_exo()
				tent = 0
	
	
	
	

def menu_criptomoedas():
	print("\033[1m...\033[m"*34,"\n")
	print(("""				●  CRIPTOMOEDAS  ●
					
			|	\033[1;36m[ \033[m1\033[1;36m ]\033[m -  BTC		|
			|	\033[1;36m[ \033[m2\033[1;36m ]\033[m -  LTC		|
			|	\033[1;36m[ \033[m3\033[1;36m ]\033[m -  ETH		|
			|	\033[1;36m[ \033[m4\033[1;36m ]\033[m -  DODGE		|
"""))
	print("\033[1m...\033[m"*34,"\n")
	tent = 0
	while True:
		try:
			print("\n")
			opc = int(input("  ◇   Escolha uma moeda :  "))
			if opc == 1 or opc == 2 or opc == 3 or opc == 4:
				print("\n")
				conversoes.clear()
				moeda = float(input("  •  Seu Dinheiro [ BRL ] : "))
				cambio = float(cotacao[f"{criptomoedas[opc-1]}"]["bid"])
				convert = moeda * cambio
				print("\n")
				print(f"  ◇  Dinheiro : R${moeda:.2f}   //   Convertido[{criptomoedas[opc-1]}] : {convert:.2f}")
				print("\n")
				p  = " "
				r = str(opc)
				name_coin = r.replace(f"{r}", f"{criptomoedas[opc-1]}")
				conversoes["BRL"] = moeda
				conversoes[f"{name_coin}"] = name_coin
				conversoes["Conversão"] = f"{convert:.3f}"
				final = conversoes.copy()
				response.append(final)
				moeda_str.append(conversoes[f"{name_coin}"])
				conversoes.clear()
				while p not in "SN":
					p = str(input("  ■  Deseja Voltar ao Menu Inicial [ S / N ] ? :")).upper()
					if p in "S":
						os.system("clear")
						inicio()
						
					elif p in "N":
						os.system("clear")
						menu_criptomoedas()
					
			if opc > 4 or opc < 1:
				tent += 1
				print(f"\033[1;31m  •  Escolha inválida : {opc} inexistente no sistema.  \033[m")
			if tent == 3:
				os.system("clear")
				menu_criptomoedas()
				tent = 0
		except ValueError as erro:
			tent += 1
			print(f"\033[1;31m  •  Escolha inválida.  \033[m")
			if tent == 3:
				os.system("clear")
				menu_criptomoedas()
				tent = 0








def inicio():
	print("\033[1m...\033[m"*34,"\n")
	print(("""
	\033[1;m		●  BEM-VINDO AO  ONVERSOR UNIVERSAL DE MOEDAS  ● \033[m
				
					
			|	\033[1;36m[ \033[m1\033[1;36m ]\033[m -  MOEDAS COMUNS		|
			|	\033[1;36m[ \033[m2\033[1;36m ]\033[m -  MOEDAS EXÓTICAS	|
			|	\033[1;36m[ \033[m3\033[1;36m ]\033[m -  CRIPTOMOEDAS		|
			|	\033[1;36m[ \033[m4\033[1;36m ]\033[m -  SAIR			|

"""))
	print("\033[1m...\033[m"*34,"\n")
	cls = 0
	while True:
		escolha = " "
		while escolha != 4:
			try:
				escolha = int(input("\n  •  Para qual categoria desejas cambear? : "))
				if escolha == 1:
					print("\n")
					menu_comum()
				elif escolha == 2:
					menu_exo()
				elif escolha == 3:
					menu_criptomoedas()
				if escolha == 4:
					print("\033[1m  •  Encerrando o sistema...\033[m")
					time.sleep(1)
					os.system("clear")
					pergunta = " "
					clear = 0
					while pergunta not in "SN" and len(pergunta) != 0:
						clear += 1
						pergunta = str(input("  ■  Antes de encerrar o sistema, gostaria de ver as conversões que foram feita [ S / N ] ? ")).upper()
						os.system("clear")
						if pergunta in "S":
							tabela= PrettyTable( [
							"\033[1;36m ENTRADA (BRL) \033[1;32m" ,
							"\033[1;33m CAMBIAMENTO (MOEDA) \033[m ",
							"\033[1;32m CONVERSÃO \033[m"])
							cont = 0
							for y in response:
								cont+=1
								for c in range(1):
									tabela.add_row([
									"\033[1;36m" + f'{y["BRL"]:^30}' + "\033[m" ,
									"\033[1;33m" + f'{moeda_str[cont-1]:^30}' + "\033[m" ,
									"\033[1;32m" + f'{y["Conversão"]:^30}' + "\033[m" ,
													])
							print(tabela)
							print("..."*34,"\n"*2)
							sys.exit()
						if clear == 3:
							os.system("clear")
							clear = 0
						elif pergunta in "N":
							sys.exit()
				if escolha > 4 or escolha < 1 or escokha != int(escolha):
					cls += 1
					print(f"\033[1;31m  •  Escolha inválida : {escolha} inexistente no sistema.  \033[m")
				if cls == 3:
					os.system("clear")
					inicio()
					cls = 0
			except ValueError as erro:
				cls += 1
				print(f"\033[1;31m  •  Escolha inválida.  \033[m")
				if cls == 3:
					os.system("clear")
					inicio()
					cls = 0



inicio()
