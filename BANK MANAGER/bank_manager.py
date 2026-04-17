#BANK MANAGEMENT SYSTEM

import math
import re
import sys
import secrets
import string
import random

def generate_account_number():
   return ''.join(secrets.choice(string.digits) for _ in range(10))

def generate_pin_number():
   return ''.join(secrets.choice(string.digits) for _ in range(5))
  

system_database = {}

def safe_input(prompt):
    while True:
       data_guard = input(prompt).strip()
       if data_guard.lower() == 'quit':
         print('Exiting the programme')
         sys.exit()

       if data_guard == '':
         print('Error, You need to enter something valid!')
         continue

       return data_guard
    
def create_accounts():
    account_number = generate_account_number()

    pin_number = generate_pin_number()

    user_name = safe_input('Enter your name: ').title()
    while not re.fullmatch(r"[A-Za-z '-]+", user_name):
       print("Name can't contain numbers and special characters!")
       user_name = safe_input('Enter your name: ').title()

    user_surname = safe_input('Enter your surname: ')
    while not re.fullmatch(r"[A-Za-z '-]+", user_surname):
     user_surname = safe_input('Enter your name: ').title()

    identity_document = safe_input('Enter your official identity document number: ')
    while not identity_document.isdigit():
        print('ID must contain only numbers.')
        identity_document = safe_input('Enter your official identity document number: ')
        

    user_id = safe_input('Your id: ')

    account = {
        "account_id": account_number,
        "pin": pin_number,
        "name": user_name,
        "surname": user_surname,
        "id_doc": identity_document,
        "id": user_id,
        "balance": 0,
        "active": True
    }

    

    system_database[account_number] = account

    print('ACCOUNT CREATED SUCCESSFULLY')
    print(f"Account info: {account}")

def get_balance():
  for user_id in system_database:
    print(f"USER ID: {user_id}")
    user_data = system_database[user_id]
    print(f"USER NAME: {user_data['name']}")
    print(f"USER SURNAME: {user_data['surname']}")
    print(f"USER ID-DOCUMENT: {user_data['id_doc']}")
    print(f"BALANCE: {user_data['balance']}")

def deposit():
  while True:

     account_number = safe_input("Enter the account number: ")
     if account_number in system_database:
        print(f"ACCOUNT NUMBER: {account_number}")
        user_data = system_database[account_number]
        print(f"USER NAME: {user_data['name']}")
        print(f"USER SURNAME: {user_data['surname']}")
        print(f"USER ID-DOCUMENT: {user_data['id_doc']}")
        print(f"BALANCE: {user_data['balance']}")

        amount = safe_input("Enter the amount in RANDS or ('q to quit'): ")
        total = user_data['balance']
        amount = int(amount)
        new_balance = total + amount

        user_data['balance'] = new_balance
        
        print(f"Successfully deposited R{amount} into {account_number}")
        print(f"NEW BALANCE: R{user_data['balance']}")

        break

def withdraw():
  while True:
     account_number = safe_input("Enter the account number you want to withdraw from ('q to quit'): ")
     if account_number in system_database:
        print(f"ACCOUNT NUMBER: {account_number}")
        attempts = 3
        user_data = system_database[account_number]
        while attempts > 0:
            
            pin_number = safe_input("Enter the pin code: ")  
            if pin_number == user_data['pin']:
                  print(f"BALANCE: {user_data['balance']}")
                  try:
                        withdrawal_amount = int(safe_input("Enter the withdrawal amount: "))
                  except ValueError:
                        print("Invalid amount. Please enter a number.")
                        continue
                  withdrawal_amount = int(safe_input("Enter the withdrawal amount: "))
                  if withdrawal_amount > user_data['balance']:
                     print('INSUFICIENT FUNDS!')
                     
                  else:
                     new_balance = user_data['balance'] - withdrawal_amount
                     print(f"SUCCESSFULLY WITHDRAWN {withdrawal_amount}")
                     
                     user_data['balance'] = new_balance
                     print(f"BALANCE: {user_data['balance']}")
                     break

            else:
               print('Wrong pin!')
               attempts -= 1

        if attempts == 0:
         print('You have exceeded the number of attempts!')
         print('Account locked temporaly, visit your nearest branch.')

        break
   

def transfer():
  while True:
  
      sender_account = safe_input("Enter the account to transfer from ('q to quit'): ")
      if sender_account in system_database:
         print(f"ACCOUNT NUMBER: {sender_account}")
         attempts = 3
         user_data = system_database[sender_account]
         while attempts > 0:
               user_pin = safe_input('Enter your pin number associated with the account number: ')
               if user_pin == user_data['pin']:
                  receiver_account = safe_input('Enter the destination account: ')
                  if receiver_account in system_database:
                     print(f"RECIEPIENT ACCOUNT: {receiver_account}")
                     try:
                           amount = safe_input('Enter the amount to transfer: ')
                     except ValueError:
                           print('Invalid amount please enter a valid number to continue')
                           continue
                     amount = float(amount)
                     if amount > user_data['balance']:
                              print('INSUFFICIENT FUNDS!')
                     elif amount <= user_data['balance']:
                              new_balance = user_data['balance'] - amount
                              print(f"SUCCESSFULLY TRANSFERRED: R{amount} to RECIEVER'S ACCOUNT {receiver_account} {user_data['name']}")
                              print(f"SENDERS ACCOUNT BALANCE: {new_balance}")
                              receiver_account = user_data['balance']
                              print(f"RECIEVER ACCOUNT: {receiver_account}")
                              print(f"AMOUNT RECEIVED: {amount}")
                              
                              print(receiver_account)
                              print(f"NAME: {user_data['name']}")

                  else:
                        print(f"Wrong pin, try again {attempts} attempts left")
                        attempts -= 1

                  break
                     
        
def exit_programm():
  return

#THE MANAGER FUNCTIONSMANAGEMENT SYSTEM CONTROL
def toggle_account_status():
  pass

def audit_total_bank_value():
  pass

print('WELCOME TO THE BANKING SYSTEM')
print('-----CHOOSE WHAT YOU NEED TO PERFOM HERE-----')
print('\n')

def print_menu():
    print("\n------MENU------")
    print("\n")
    print(f"1. CREATE ACCOUNT")
    print(f"2. VIEW BALANCES")
    print(f"3. DEPOSIT MONEY")
    print(f"4. WITHDRAW CASH")
    print(f"5. TRANSFER MONEY")
    print(f"6. EXIT")

while True:
   print_menu()

   print('\n')
   choice = safe_input("select from the menu: ")
   if choice not in ['1', '2', '3', '4', '5', '6']:
      print('Wrong selection, choose from the `menu-option`')
      continue

   if choice == '1':
      create_accounts()

   elif choice == '2':
      print('\n')
      get_balance()

   elif choice == '3':
      deposit()
    
   elif choice == '4':
      withdraw()
    
   elif choice == '5':
      transfer()

   elif choice == '6':
      print('THANKS FOR USING OUR SERVICES, GOODBYE!')
      break