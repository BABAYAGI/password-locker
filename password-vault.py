#!/usr/bin/env python3.6
# import pyperclip
from owner import owner 
from owner import Credentials
import random

def create_user(user_name, password):
    '''
    Function to create a new contact
    '''
    new_user = owner(user_name, password)
    return new_user


def save_user(owner):
    '''
    Function to save owner
    '''
    owner.save_user()


def create_credential(user_name ,account_name , password):
    '''
    Function that creates new credentials.
    '''
    new_credential = Credentials(user_name ,account_name , password)
    return new_credential


def save_credential(credential):
    '''
    Function to save a newly created credential.
    '''
    Credentials.save_credentials(credential)

def display_credentials(user_name):
    '''
    Function that returns saved credentials
    '''
    return Credentials.display_credentials(user_name)

def delete_credentials(Credentials):
    '''
    Function that deletes a credential
    '''
    Credentials.delete_credential()


def find_by_account_name(account_name):
    '''
    Function that finds by account name.
    '''
    return Credentials.find_by_account_name(account_name)

def copy_credential(account_name):
    '''
    Function that copies credentials details.
    '''
    return Credentials.copy_credential(account_name)

def delete_credential(credential):
    '''
    Function that deletes credentials.
    '''
    credential.delete_credential()

def check_credentials(account_name):
    '''
    Function that checks if a credential exists.
    '''
    return Credentials.credential_exist(account_name)\


def main():
    print("Hello Welcome to Password - vault.")
    user_name = input("Enter a username ----")
    password = input("Enter your password ----")

    print('/no')
    print(f"Brilliant Agent {user_name}. Your in !!")
    print('/no')
    print(f"LOGIN SUCCESSFUL {user_name} Let's get to it.")
    print('/no')

    while True:
            print("Use these short codes : ac - Add new credentials,  dc - display credentials,  fc -find a credentials, ex -exit the app")

            short_code = input().lower()
            Credentials=""
            if short_code == 'ac':
                print("New credentials")
                print("-"*10)

                print("owner name ...")
                user_name = input('******')

                print("Account ...")
                account_name = input('******')

                print("Password ...")
                print('\n')
                print("Would you like to generate a password ? (yes/no)")
                answer = input('******')
                if answer == 'yes':
                    print("Enter length of the password :")
                    length = int (input('******'))
                    chars = "QWERTYUIOPLKJHGGFDDASZXCVBNMqwertyuuioplkjhgfddssazxcvbnnm,."":lkp{[}[!@#$%^&*()"
                    password = ''

                    for _ in range (length):
                        password += random.choice(chars)    
                    print (password)
                    # return password
                    
                    
                elif answer == 'no':
                    print("Enter your preferred password :")
                    password = input('******')
                # create and save new contact.
                save_credential(create_credential(user_name, account_name, password))
                print('\n')
                print(f"New Credential {user_name} {account_name} created")
                print('\n')   

            elif short_code == 'dc':

                if display_credentials(user_name):
                    print("Here is a list of all your credentials")
                    print('\n')

                    for Credentials in display_credentials(user_name):
                        print(
                            f"owner NAME ****** {Credentials.user_name} ACC NAME ******{Credentials.account_name} PASS ****** {Credentials.account_password}")

                    print('/no')
                else:
                    print('/no')
                    print("You dont seem to have any credentials saved yet")
                    print('/no')

            elif short_code == 'fc':

                print("Enter the account you want to search for")

                search_account = input()
                if check_credentials(search_account):
                    search_account = find_by_account_name(search_account)
                    print(f"{search_account.user_name} {search_account.user_name}")
                    print('-' * 20)

                    print(f"owner name.......{search_account.user_name}")
                    print(f"Account name.......{search_account.account_name}")
                else:
                    print("That credential does not exist")
                    print('/no')
            elif short_code == "ex":
                print("Cheers Mate .......")
                break
            else:
                print("I didn't quite get that. Please do use the short codes")


if __name__ == '__main__':

    main()