import requests
import json
import time
import os
import platform 
from datetime import datetime
try:
	from colorama import Fore
except:
	os.system('pip install colorama')

while(True):
	r = requests.get('https://api.moonpay.com/v3/currencies/ask_price?cryptoCurrencies=btc,eth,usdt&fiatCurrencies=usd,pln,eur,gbp,jpy&apiKey=pk_live_QWvwDl3WJAq7S8fDjsOUMfjn09DSw8R')
	r = r.json()
	btc_eur = r['BTC']['EUR']
	btc_usd = r['BTC']['USD']
	btc_gbp = r['BTC']['GBP']
	btc_jpy = r['BTC']['JPY']
	btc_pln = r['BTC']['PLN']
	eth_eur = r['ETH']['EUR']
	eth_usd = r['ETH']['USD']
	eth_gbp = r['ETH']['PLN']
	eth_jpy = r['ETH']['JPY']
	eth_pln = r['ETH']['PLN']
	usdt_eur = r['USDT']['EUR']
	usdt_usd = r['USDT']['USD']
	usdt_gbp = r['USDT']['GBP']
	usdt_jpy = r['USDT']['JPY']
	usdt_pln = r['USDT']['PLN']
	if(platform.system().lower()=="windows"):
		cmd='cls'
	else:
		cmd='clear'
	os.system(cmd)
	now = datetime.now()
	print()
	print(f'                  {Fore.RED}{now.strftime(f"%H{Fore.WHITE}:{Fore.RED}%M{Fore.WHITE}:{Fore.RED}%S")}{Fore.WHITE}')
	print()
	print(f'=============================================')
	print(f'                  {Fore.YELLOW}BTC {Fore.WHITE}PRICE                  ')
	print(f'=============================================')
	print(f'EUR: {Fore.YELLOW}{btc_eur}{Fore.WHITE} €{Fore.WHITE}')
	print(f'USD: {Fore.YELLOW}{btc_usd}{Fore.WHITE} ${Fore.WHITE}')
	print(f'GBP: {Fore.YELLOW}{btc_gbp}{Fore.WHITE} £{Fore.WHITE}')
	print(f'PLN: {Fore.YELLOW}{btc_pln}{Fore.WHITE} zł{Fore.WHITE}')
	print(f'JPY: {Fore.YELLOW}{btc_jpy}{Fore.WHITE} ¥{Fore.WHITE}')
	print(f'=============================================')
	print(f'                  {Fore.CYAN}ETH {Fore.WHITE}PRICE                  ')
	print(f'=============================================')
	print(f'EUR: {Fore.CYAN}{eth_eur}{Fore.WHITE} €{Fore.WHITE}')
	print(f'USD: {Fore.CYAN}{eth_usd}{Fore.WHITE} ${Fore.WHITE}')
	print(f'GBP: {Fore.CYAN}{eth_gbp}{Fore.WHITE} £{Fore.WHITE}')
	print(f'PLN: {Fore.CYAN}{eth_pln}{Fore.WHITE} zł{Fore.WHITE}')
	print(f'JPY: {Fore.CYAN}{eth_jpy}{Fore.WHITE} ¥{Fore.WHITE}')
	print(f'=============================================')
	print(f'                 {Fore.GREEN}USDT {Fore.WHITE}PRICE                  ')
	print(f'=============================================')
	print(f'EUR: {Fore.GREEN}{usdt_eur}{Fore.WHITE} €{Fore.WHITE}')
	print(f'USD: {Fore.GREEN}{usdt_usd}{Fore.WHITE} ${Fore.WHITE}')
	print(f'GBP: {Fore.GREEN}{usdt_gbp}{Fore.WHITE} £{Fore.WHITE}')
	print(f'PLN: {Fore.GREEN}{usdt_pln}{Fore.WHITE} zł{Fore.WHITE}')
	print(f'JPY: {Fore.GREEN}{usdt_jpy}{Fore.WHITE} ¥{Fore.WHITE}')
	time.sleep(1)