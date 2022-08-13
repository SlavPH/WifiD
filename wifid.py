#!/usr/bin/env python3

# Github   : https://github.com/SlavPH 
# Telegram : https://telegram.me/SlavPH

# LIbraries
import os
import sys

# Colors
black='\033[1;90m'      # Black
red='\033[1;91m'        # Red
green='\033[1;92m'      # Green
yellow='\033[1;93m'     # Yellow
blue='\033[1;94m'       # Blue
purple='\033[1;95m'     # Purple
cyan='\033[1;96m'       # Cyan
white='\033[1;97m'      # White
reset='\033[0m'         # Reset

# Clear Terminal
os.system("clear")

# Icon
icon = (f"""
{blue}         .__  _____.__ {red} ________    
{blue} __  _  _|__|/ ____\__|{red} \______ \   
{blue} \ \/ \/ /  \   __\|  |{red}  |    |  \  
{blue}  \     /|  ||  |  |  |{red}  |    `   \ 
{blue}   \/\_/ |__||__|  |__|{red} /_______  / 
{green}   Simple Wifi Manager{red}         \/ 
{green}   By SlavPH
{reset}
""")

# Menu
menu = (f"""
{red}[1] {green}Show interfaces
{red}[2] {green}Turn wifi on
{red}[3] {green}Turn wifi off
{red}[4] {green}Show wifi devices 
{red}[5] {green}Connect to wifi 
{red}[0] {green}Exit 
{reset}
""")

print(icon)
print(menu)

# Main Function
def main():

    # input option
    option = input(f"\n{cyan}Choose your option : {reset}")

    if option == "1":
        os.system("nmcli d")
        main()

    elif option == "2":
        os.system("nmcli r wifi on")
        main()

    elif option == "3":
        os.system("nmcli r wifi off")
        main()

    elif option == "4":
        os.system("nmcli d wifi list")
        main()

    elif option == "5":
        ssid   = input(f"\n {yellow}[*] Enter the wifi name : {red}")
        passwd = input(f"\n {yellow}[*] Enter the password  : {red}")
        print(f"{reset}\n")
        os.system(f"nmcli d wifi connect {ssid} password {passwd}")    
        main()

    elif option == "0":
        sys.exit()

    else:
        try:
            print(f"{red}Wrong option! try again!{reset}")
            menu()
        except Exception as e:
            print(f"{red}{e}")  

if __name__ == "__main__":
   main()
