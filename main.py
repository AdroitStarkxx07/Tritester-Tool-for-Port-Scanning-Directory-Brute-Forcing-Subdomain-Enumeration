import threading
from queue import Queue
import requests
import random
import sys
import socket
import time
from datetime import datetime


def port_scanner(host_name):
    
    print_lock = threading.Lock()
    
    #Defining target
    target = socket.gethostbyname(host_name) #Translating hostname to IPv4


    #Adding a banner
    print("-" * 50)
    print("Starting Scan")
    print("scanning target " +target)
    print("Time Started :" +str(datetime.now()))
    print("-" * 50)

    def pscan(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            with print_lock:
                if result == 0:
                    print("PORT {} IS OPEN".format(port))
            s.close()

        except KeyboardInterrupt:
            print("\n Exiting Program. ")
            sys.exit()

        except socket.gaierror:
            print("Hostname could not be resolved. ")
            sys.exit()
        
        except socket.error:
            print("Couldn't connect to server. ")
            sys.exit()

    def threader():
        while True:
            worker=q.get()
            pscan(worker)
            q.task_done()

    q= Queue()

    for x in range(50):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

    for worker in range(1,500):
        q.put(worker)

    q.join()



def brute_force(website, urlp, wordlistp, extp):
    
    url=urlp
    wordlist=wordlistp
    ext=extp

    try:
        target = socket.gethostbyname(website) #Translating hostname to IPv4

    except socket.gaierror:
        print("Hostname could not be resolved. ")
        sys.exit()
        
    except socket.error:
        print("Couldn't connect to server. ")
        sys.exit()

    #Adding a banner
    print("-" * 50)
    print("Starting Scan")
    print("scanning target " +target)
    print("Time Started :" +str(datetime.now()))
    print("-" * 50)

    def write(word):
        f1 = open("write1.txt","a")
        f1.write(word +"\n")
        
    fo = open(wordlist,"r+")
    for i in range(1000):
        word = fo.readline(10).strip()
        surl = url+word+ext
            
        response = requests.get(surl)
        if (response.status_code == 200):
            print ("[+] found :- ",surl)
            write(word)
        else:
            print ("[-] Not found :- ",surl)
            pass


def subdomain(website):
    
    domain = website

    try:
        target = socket.gethostbyname(website) #Translating hostname to IPv4

    except socket.gaierror:
        print("Hostname could not be resolved. ")
        sys.exit()
        
    except socket.error:
        print("Couldn't connect to server. ")
        sys.exit()

    #Adding a banner
    print("-" * 50)
    print("Starting Scan")
    print("scanning target " +target)
    print("Time Started :" +str(datetime.now()))
    print("-" * 50)


    file = open("Subdomain.txt")
    content = file.read()
    subdomains = content.splitlines()

    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            requests.get(url)
            
        except requests.ConnectionError:
            pass
        else:
            print("[+] Discovered subdomain:", url)


if __name__ == '__main__':

    while True:
        
        print("*" * 50)
        print('\n Welcome to the TriTester ! \n')
        print("*" * 50)

        print('Enter 1 for Port Scanner \n')

        print('Enter 2 for Directory Bruteforcer \n')

        print('Enter 3 for Subdomain Enumerator \n')

        ch= 1        

        while(ch != 0):

            choice = int(input('\n Enter your choice: '))

            if (choice == 1):
            
                print(" \n You have entered the Port Scanner !! \n ")

                website= (input("Enter target : "))
                print("\n")
                port_scanner(website)
                print("-" *50)
                print("scan completed succesfully")
                print("Time Completed: " +str(datetime.now()))
                print("-" *50)

            elif (choice == 2):
            
                print(" \n You have entered the Directory Bruteforcer !! \n ")
            
                website= (input("Enter target website : "))
                url= (input("\n Enter target URL : "))
                wordlist= (input("\n Enter wordlist : "))
                extension= (input("\n Enter extension : "))
                print("\n")
                brute_force(website, url,wordlist,extension)
                print("-" *50)
                print("scan completed succesfully")
                print("Time Completed: " +str(datetime.now()))
                print("-" *50)

            elif (choice == 3):
            
                print(" \n You have entered the Subdomain Enumerator !! \n ")

                website= (input("Enter domain : "))
                subdomain(website)
                print("-" *50)
                print("scan completed succesfully")
                print("Time Completed: " +str(datetime.now()))
                print("-" *50)

            else:
                print('Invalid choice')

        
            ch=int(input("\n Press 0 to exit or any other number key to continue : "))

        print("\n Good Bye ! \n")
        exit()




