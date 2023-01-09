# Import modules
import whois
import pyfiglet
import datetime
import sys
import os
from termcolor import colored
from pyfiglet import figlet_format

# Rearrange screen
os.system('clear')

#Banner
print((colored(figlet_format("HellCat"), color="red")))

# Signature
print('\033[32;1m')
print('By: Sh0gun')
print('\033[m')

# Workflow

domain = whois.whois(input("Enter Your Target:https:// "))
data ={

	'expiration_date': datetime.datetime(2020, 9, 14, 0, 0),
	'last_updated': datetime.datetime(2011, 7, 20, 0, 0),
	'registrar': 'MARKMONITOR INC.',
	'name': domain,
	'creation_date': datetime.datetime(1997, 9, 15, 0, 0)


}
print(data)
