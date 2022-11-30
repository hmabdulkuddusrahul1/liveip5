import random, time, platform

from colorama import Fore
from pystyle import Colorate, Colors

# main functions from main file

import main

def iprange():
    main.clear()

    print(Colorate.Horizontal(Colors.yellow_to_green, '\nSkCracker » Input your IP list\n'))

    list = input(Colorate.Horizontal(Colors.yellow_to_green, f"root@{platform.system()}:~/SkCracker# » "))

    print(Colorate.Horizontal(Colors.yellow_to_green, '\nSkCracker » Generating IPs...'))

    try:
        total = open(list, 'r').readlines()
    except:
        main.clear()

        print(Colorate.Horizontal(Colors.yellow_to_green, '\nSkCracker » Wrong selection! try again'))

        print(Colorate.Horizontal(Colors.yellow_to_green, "\n Returning in 3 seconds..."))

        time.sleep(3)

        main.main()

    try:
        for ips in total:
            ips = ips.strip()
            part = ips.split('.')

            for j in range(0, 256):
                for k in range(0, 256):
                    ranged = part[0] + "." + part[1] + "." + str(j) + "." + str(k)
                    open('rangeds.txt', 'a').write(ranged + '\n')

            main.clear()

            print(Colorate.Horizontal(Colors.yellow_to_green, '\nSkCracker » [+] GENERATED IPS AND SAVED IN ip.txt!'))

            print(Colorate.Horizontal(Colors.yellow_to_green, "\n Returning in 3 seconds..."))

            time.sleep(3)

            main.main()
    except:
        main.clear()

        print(Colorate.Horizontal(Colors.yellow_to_green, '\nSkCracker » [+] GENERATED IPS AND SAVED IN ip.txt!'))

        print(Colorate.Horizontal(Colors.yellow_to_green, "\n Returning in 3 seconds..."))

        time.sleep(3)

        main.main()