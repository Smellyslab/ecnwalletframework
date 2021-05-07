import requests
import os
import json
import sys
import time





wallets = open('wallet.txt', 'r')
wallet = wallets.read()
keys = open('key.txt', 'r')
key = keys.read()

def run():
  try:
    while True:
      choice = input('enter a command "help or ? for help": ')
      if choice.lower() == "help":
        print('              Commands Are            ')
        print('======================================')
        print('bal // tells you your wallets balance')
        print('mine // mines a block to you adress')
        print('newtransaction // makes a new transaction')
        print('clear // clears the screen')
        print('generatewallet // makes a new wallet and tells you thing info // dont lose or share the private key!')
        print('======================================')
      elif choice == "?":
        print('              Commands Are            ')
        print('======================================')
        print('bal // tells you your wallets balance')
        print('mine // mines a block to you adress')
        print('newtransaction // makes a new transaction')
        print('clear // clears the screen')
        print('generatewallet // makes a new wallet and tells you thing info // dont lose or share the private key!')
        print('======================================')
      elif choice.lower() == 'bal':
        output = requests.get(f'https://econcoin.pythonanywhere.com/getwalletbal/{wallet}')
        print(f'wallets bal is: {output.text}')
      elif choice.lower() == 'mine':
        output = requests.get(f'https://econcoin.pythonanywhere.com/mine/{wallet}')
        binarys = output.content
        json_data = json.loads(binarys)
        print("============Mined A New Block============")
        print(f"Block Number: {json_data[0]['index']}")
        print(f"Previous Block Hash: {json_data[0]['previous_hash']}")
        print(f"Block Proof of work number: {json_data[0]['proof']}")
        print(f"Block Mining reward [if it says anything over 5 you got anywhere from 0,5 coins its just showing the recent transaction value]: {json_data[0]['transactions'][0]['amount']}")
        print("============Mined A New Block============")
      elif choice.lower() == 'newtransaction':
        adress = input('Address to send ECN to: ')
        amount = input('Amount of ECN to send: ')
        output = requests.get(f'https://econcoin.pythonanywhere.com/transaction/new/{wallet}/{key}/{adress}/{amount}')
        print(output.text)
      elif choice.lower() == "clear":
        os.system("clear||cls")
      elif choice.lower() == "generatewallet":
        output = requests.get('https://econcoin.pythonanywhere.com/wallet/new')
        binarys = output.content   
        json_data = json.loads(binarys)
        print(f"New wallets adress: {json_data['address']}")
        print(f"New wallets private key: {json_data['key']}")
        print("Dont share the private key with anyone, and dont lose it save these in something a .txt file or notes...")
      elif choice.lower() == "exit":
        print("Thanks for using ECN!")
        time.sleep(2)
        os.system("clear||cls")
        sys.exit()
      elif choice.lower() == "quit":
        print("Thanks for using ECN!")
        time.sleep(2)
        os.system("clear||cls")
        sys.exit()
      else:
        print(f'\033[01;31m{choice} is not a command!\033[00m')
  except Exception as e:
    print(e)      


run()
