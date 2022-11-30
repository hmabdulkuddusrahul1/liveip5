import random, time

from colorama import Fore
from pystyle import Colorate, Colors

# main functions from main file

import main

def genip():

    main.clear()

    print(Colorate.Horizontal(Colors.yellow_to_green, '\nSkCracker » Input how many IPs to generate\n'))

    nips = input(Colorate.Horizontal(Colors.yellow_to_green, "root@windows:~/SkCracker# » "))

    print(Colorate.Horizontal(Colors.yellow_to_green, '\nSkCracker » Generating IPs...'))

    ips = []

    for i in range(0, int(nips)):
        a = random.randrange(0, 255, 1)
        b = random.randrange(0, 255, 1)
        c = random.randrange(0, 255, 1)
        d = random.randrange(0, 255, 1)
        ip = str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d)
        ips.append(ip + "\n")


    towrite = ''.join(ips)


    open('ip.txt', 'a').write(towrite)

    main.clear()

    print(Colorate.Horizontal(Colors.yellow_to_green, '\nSkCracker » [+] GENERATED IPS AND SAVED IN ip.txt!'))

    print(Colorate.Horizontal(Colors.yellow_to_green, "\nReturning in 3 seconds..."))

    time.sleep(3)

    main.main()