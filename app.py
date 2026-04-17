from colorama import Fore, Style, init
import os
import botBing, checkinfo
init(autoreset=True)

def checkFile(tipe):
    tipe = tipe
    path = "./cookie/"
    if tipe == "desktop":
        files = os.listdir(path+"/"+tipe)
        print(Fore.GREEN+"-------------------------------------")
        for i, f in enumerate(files, start=1):
            print(f"{i}. {f}")
        print(Fore.GREEN+"-------------------------------------")
        print("0. Exit")
        print(Fore.GREEN+"-------------------------------------")
        try:
            pilihan = int(input("\nPilih nomor file untuk dibuka (0 untuk batal): "))

            if pilihan == 0:
                print("Batal membuka file.")
            elif 1 <= pilihan <= len(files):
                namafile = files[pilihan-1]
                try:
                    jumlahSearch = int(input("masukan jumlah pencarian: "))
                    botBing.startBot(namafile, "desktop", jumlahSearch)
                except ValueError:
                    print(Fore.RED + "[x] Pilihan tidak valid!")                    
            else:
                print(Fore.RED + "[x] Pilihan tidak valid!")
        except ValueError:
            print(Fore.RED + "[x] Pilihan tidak valid!")
    elif tipe == "mobile":
        files = os.listdir(path+"/"+tipe)
        for i, f in enumerate(files, start=1):
            print(f"{i}. {f}")
        try:
            pilihan = int(input("\nPilih nomor file untuk dibuka (0 untuk batal): "))

            if pilihan == 0:
                print("Batal membuka file.")
            elif 1 <= pilihan <= len(files):
                namafile = files[pilihan-1]
                try:
                    jumlahSearch = int(input("masukan jumlah pencarian: "))
                    botBing.startBot(namafile, "mobile", jumlahSearch)
                except ValueError:
                    print(Fore.RED + "[x] Pilihan tidak valid!")
            else:
                print(Fore.RED + "[x] Pilihan tidak valid!")
        except ValueError:
            print(Fore.RED + "[x] Pilihan tidak valid!")
    else:
        print("tidak ada")


def menu_utama():
    print(Fore.RED +"""
        8       o              88 
        8                      88 
        8oPYo. o8 odYo. .oPYo. 88      _________________________
        8    8  8 8' `8 8    8 88     |                         |
        8    8  8 8   8 8    8 `'     |   Browser Automation    |
        `YooP'  8 8   8 `YooP8 88     |   Version: r2.1 Beta    |
        :.....::....::..:....8 ...    |_________________________|
        ::::::::::::::::::ooP'.:::
        ::::::::::::::::::...:::::
""")
    while True:
        
        print("------------------------------")
        print("1. Start Bot Search")
        print("2. Check Info")
        print("3. Check Mission")

        print("0. Exit")
        print("------------------------------")
        print("\n")
        pilihan = input(Fore.BLUE + "bing"+Fore.WHITE+">: ")

        if pilihan == "0":
            print("Keluar dari program.")
            break
        elif pilihan == "1":
            startBot() 
        elif pilihan == "2":
            files = os.listdir("./cookie/rewards")
            print(Fore.GREEN+"-------------------------------------")
            for i, f in enumerate(files, start=1):
                print(f"{i}. {f}")
            print(Fore.GREEN+"-------------------------------------")
            print("0. Exit")
            print(Fore.GREEN+"-------------------------------------")
            try:
                pilihan = int(input("\nPilih nomor file untuk dibuka (0 untuk batal): "))

                if pilihan == 0:
                    print("Batal membuka file.")
                elif 1 <= pilihan <= len(files):
                    namafile = files[pilihan-1]
                    checkinfo.checkBotInfo(namafile)
                else:
                    print(Fore.RED + "[x] Pilihan tidak valid!")
            except ValueError:
                print(Fore.RED + "[x] Pilihan tidak valid!")
        elif pilihan == "3":
            files = os.listdir("./cookie/rewards")
            print(Fore.GREEN+"-------------------------------------")
            for i, f in enumerate(files, start=1):
                print(f"{i}. {f}")
            print(Fore.GREEN+"-------------------------------------")
            print("0. Exit")
            print(Fore.GREEN+"-------------------------------------")
            try:
                pilihan = int(input("\nPilih nomor file untuk dibuka (0 untuk batal): "))

                if pilihan == 0:
                    print("Batal membuka file.")
                elif 1 <= pilihan <= len(files):
                    namafile = files[pilihan-1]
                    checkinfo.checkMission(namafile)
                else:
                    print(Fore.RED + "[x] Pilihan tidak valid!")
            except ValueError:
                print(Fore.RED + "[x] Pilihan tidak valid!")
        else:
            print(Fore.RED + "[x] Pilihan tidak valid!")

def startBot():
    while True:
        print("1. Desktop")
        print("2. Mobile")
        print("0. Back")

        startBotPilihan = input(Fore.BLUE + "bing"+Fore.WHITE +">>"+ Fore.BLUE + "startbot"+Fore.WHITE+">: ")

        if startBotPilihan == "0":
            os.system("cls")
            break
            
        elif startBotPilihan == "1":
            checkFile(tipe="desktop")
        elif startBotPilihan == "2":
            checkFile(tipe="mobile")
        else:
            print(Fore.RED + "[x] Pilihan tidak valid!")



menu_utama()

