from concurrent.futures import thread
import requests 
import random
import string
import time
from colorama import *
import os

os.system('cls')

valid_counter = 0



def random_unvalid(length, color, text):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    print(f"{Fore.MAGENTA} [ - ] {Fore.RESET}{Fore.BLUE}BTC ADRESS{Fore.RESET}   :   {color} 0x{result_str} {Fore.RESET}{color} {Fore.MAGENTA} [{Fore.RESET} {text} {Fore.MAGENTA}] {Fore.RESET}")


def main():
    global valid_counter

    main_ascii = """
                                             _ _ _     _ _     _      _____ _             
                                            | | | |___| | |___| |_   |     |_|___ ___ ___ 
                                            | | | | .'| | | -_|  _|  | | | | |   | -_|  _|                                                   
                                            |_____|__,|_|_|___|_|    |_|_|_|_|_|_|___|_| 
    """

    random_btc = random.uniform(0.5, 1)
    print(f" {Fore.LIGHTMAGENTA_EX} {main_ascii} {Fore.RESET}")
    wallet_adress = str(input(f"{Fore.MAGENTA} [ - ] {Fore.RESET}{Fore.BLUE}Your Wallet Adress  {Fore.RESET} :   "))

    percentage_chance = 0.00001 # The smaller the number the less likely you are to find a valid, ex : 0.01 = more chance than 0.000000000000001
    counter = [1]

    for i in counter:
        counter.append(i + 1)
        for a in range (1):
            (random_unvalid(35, Fore.RED, "NOT VALID"))
            os.system(f"title Wallet checked : {i} / Valid found Wallet : {valid_counter}")

        if random.random() < percentage_chance:
            (random_unvalid(35, Fore.GREEN, "  VALID  "))
            valid_counter += 1
            os.system(f"title Wallet checked : {i} / Valid found Wallet : {valid_counter}")
            time.sleep(0.01)
            print(f"{Fore.MAGENTA} [ - ] {Fore.RESET}{Fore.BLUE}You mined{Fore.RESET}    :    {Fore.GREEN}{random_btc} BTC{Fore.RESET}")
            time.sleep(0.5)
            print(f"{Fore.MAGENTA} [ - ] {Fore.RESET}{Fore.BLUE}Transaction{Fore.RESET}  :    {Fore.GREEN}{random_btc} BTC{Fore.RESET}\n{Fore.MAGENTA} [ - ] {Fore.RESET}{Fore.BLUE}Please wait...{Fore.RESET}")
            time.sleep(3.5)
            time.sleep(5)
            asker = str(input(f"{Fore.MAGENTA} [ - ] {Fore.RESET}{Fore.BLUE}Do you want to relunch ? : [ Y / N ] : {Fore.RESET}"))
            if asker.lower() == "y":
                os.system('cls||clear')
                main()
            elif asker.lower() == "n":
                print(f"{Fore.MAGENTA} [ - ] {Fore.RESET}{Fore.BLUE}See you soon !{Fore.RESET}")
            time.sleep(3)
            exit()

main()