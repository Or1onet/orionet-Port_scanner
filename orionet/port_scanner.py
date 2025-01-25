import socket

import time
import sys
import random
import os
import re
def banner():
    
    _=("_"*70)
    print(_)
    ban=("""
                      __
    ____  ____  _____/ /_   ______________ _____  ____  ___  _____
   / __ \/ __ \/ ___/ __/  / ___/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
  / /_/ / /_/ / /  / /_   (__  ) /_ / /_/ / / / / / / /  __/ /    
 / .___/\____/_/   \__/  /____/\___/\__,_/_/ /_/_/ /_/\___/_/     
/_/   
by Orionet""")
    print(ban)
    r_=("_" *70)
    print(r_)
    return _,ban,r_

banner()

start=time.time()

def porte_com(host2):
    
    try:
        for p in (20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 110, 119, 123, 137, 138, 139, 143, 161, 162, 179, 389, 443, 465, 500, 514, 515, 520, 587, 636, 993, 995, 1080, 1433, 1521, 1723, 1900, 1935, 2049, 2181, 3306, 3389, 3690, 4000, 5000, 5432, 5631, 5900, 6379, 6667, 8000, 8080, 8443, 25565, 27015, 28960, 3478, 3479, 3724, 50000):
            print(f"start scan at the port(Crtl+C to exit): {p}")
            ci=socket.socket(socket.AF_INET,socket.SOCK_STREAM,proto=0)
            con=ci.connect_ex((host2,p))
            cont=0
            cont_no=0
            if con== 0:
                print(f"the port: {p} is OPEN")
                cont +=1
                ci.close
                
            else:
                print(f"the port: {p} isn't open")
                cont_no +=1
        conteg=cont
        conteg_no=cont_no
                
        end=time.time()
        dif=start-end
        print("_" *25)
        print("SCAN COMPLETED")
        print(f"the open port are {conteg}  and the closed port are {conteg_no}")
        print(dif)
        print("_" *25)
        sys.exit()
    except KeyboardInterrupt:
        print("_" *20)
        print("""you're about to go out""")
        print("_" *20)
    
        sys.exit()  
        
def port_comm_open(host2):
    try:
        for p in (20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 110, 119, 123, 137, 138, 139, 143, 161, 162, 179, 389, 443, 465, 500, 514, 515, 520, 587, 636, 993, 995, 1080, 1433, 1521, 1723, 1900, 1935, 2049, 2181, 3306, 3389, 3690, 4000, 5000, 5432, 5631, 5900, 6379, 6667, 8000, 8080, 8443, 25565, 27015, 28960, 3478, 3479, 3724, 50000):
            ci=socket.socket(socket.AF_INET,socket.SOCK_STREAM,proto=0)
            con=ci.connect_ex((host2,p))
            cont=0
            cont_no=0
            if con== 0:
                print(f"the port: {p} is OPEN")
                cont +=1
                ci.close()
                
            else:
                cont_no +=1
                continue  
        conteg =cont
        conteg_no =cont_no
        end=time.time()
        dif=start-end
        print("_" *25)
        print("SCAN COMPLETED")
        print(f"the open port are {conteg}  and the closed port are {conteg_no}")
        print (dif)
        print("_" *25)
        sys.exit()
    except KeyboardInterrupt (conteg,conteg_no):
        print("_" *20)
        print("""you're about to go out""")
        print("_" *20)
    
        sys.exit()  
        
        
def is_valid_domain(domain):
    # Controlla se il dominio sembra valido
    regex = r'^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9-]{2,}$'
    return re.match(regex, domain) is not None

def sito_open(percor):
    try:
        cont=0
        cont_no=0
        
        percors=str(percor.strip('"').strip("'"))
        if not os.path.isfile(percors):
            print("ERROR  the specified file does not exist")
            sys.exit()
        if os.path.isfile(percors):
            print("file OK")
            
        if not percors.endswith(".txt"):
            print("the file is not with the extension .txt")
            sys.exit()
        else:
            with open(percors,"r") as file:
                    num_riga=file.readlines()
                    for element in num_riga:
                        elements=element.strip()
                        if not is_valid_domain(elements):
                            print(f"the domain {elements} is not correct")
                            continue
                    
                    
                        t4=socket.gethostbyname(elements)
                        print(f"the site {elements}  IP {t4}  is confirmed")
                        for por in (20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 110, 119, 123, 137, 138, 139, 143, 161, 162, 179, 389, 443, 465, 500, 514, 515, 520, 587, 636, 993, 995, 1080, 1433, 1521, 1723, 1900, 1935, 2049, 2181, 3306, 3389, 3690, 4000, 5000, 5432, 5631, 5900, 6379, 6667, 8000, 8080, 8443, 25565, 27015, 28960, 3478, 3479, 3724, 5000):
                            try:
                                sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM,proto=0)
                                conect=sock.connect_ex((t4,por))
                                if conect==0:
                                    cont +=1
                                    print(f"the site: {elements} is OPEN at the port {por} ")
                                    sock.close()
                                else:
                                    cont_no +=1
                                    continue
                                if conect==((elements,5000)):
                                    conteg=cont
                                    conteg_no=cont_no
                                    end=time.time()
                                    dif=start-end
                                    print("_" *25)
                                    print("SCAN COMPLETED")
                                    print(f"the open port are {conteg}  and the closed port are {conteg_no}")
                                    print(dif)
                                    print("_" *25)
                                    sys.exit()
                            except socket.gaierror:
                                    print("error regarding the host in the file")
                                    sys.exit()
        
    except KeyboardInterrupt:
        print("_" *20)
        print("""you're about to go out""")
        print("_" *20)
        sys.exit()
              
#PORT SCANNER
def port_scanner(t,port1,port2):
    try:
        for port in range(port1,port2 +1):
          print(f"""start scan at the port(Crtl+C to exit): {port} """)
          c=socket.socket(socket.AF_INET,socket.SOCK_STREAM,proto=0)
          conn=c.connect_ex((t,port))
          cont= 0
          cont_no=0
          if conn== 0:
              print(f"the port: {port} is OPEN")
              cont +=1
              
          else:
              print(f"the port: {port} isn't open")
              cont_no +=1
              
        
        conteg= cont
        conteg_no=cont_no
              
        end=time.time()
        dif=start-end
        print("_" *25)
        print("SCAN COMPLETED")
        print(f"the open port are {conteg}  and the closed port are {conteg_no}")
        print(dif)
        print("_" *25)
        sys.exit()
    except KeyboardInterrupt:
        print("_" *20)
        print("""you're about to go out""")
        print("_" *20)
        sys.exit()


        
def random_port(host3,num):
    try:
        sc=set()
        
        for _ in range(num):
            rand=random.randint(1,49151)
            if rand in sc:
                continue
            sc.add(rand)
            print(f"start scan at the port(Crtl+C to exit): {rand}")
            so=socket.socket(socket.AF_INET,socket.SOCK_STREAM,proto=0)
            conne=so.connect_ex((host3,rand))
            cont=0
            cont_no=0
            if conne== 0:
                print(f"the port: {rand} is OPEN")
                cont+=1
                so.close
                
            else:
                print(f"the port: {rand} isn't open")
                cont_no+=1
        conteg=cont
        conteg_no=cont_no      
        end=time.time()
        dif=start-end
        print("_" *25)
        print("SCAN COMPLETED")
        print(f"the open port are {conteg}  and the closed port are {conteg_no}")
        print(dif)
        print("_" *25)
        sys.exit()
              
    except KeyboardInterrupt:
        print("_" *20)
        print("""you're about to go out""")
        print("_" *20)
        sys.exit()
    

#HOST

host=(input("choose the host to scan(--help for all commands): ",))
if host =="--help":
        print("""-p=Scanning the 60 most common port
-r= Scanning 50 random port
--open= only shows the open port (matchable with -p)
-s=scan all the domains present in a file with .txt extension
""")
        sys.exit()
if host == "-p" :
    try:
        host2=(input("choose the host to scan (-p confirmed):",))
        t2=socket.gethostbyname(host2)
        print(f"IP confirmed: ",t2)
        porte_com(host2)
    except socket.gaierror:
            print("error regarding the host")
        
if host== "-r":
    try:
        host3=(input("choose the host to scan (-r confirmed):",))
        t3=socket.gethostbyname(host3)
        print(f"IP confirmed: ",t3)
        num=int(input("how many ports do you want to randomly scan:"))
        random_port(host3,num)
        sys.exit()
        if num==str:
            print("it is not possible to insert a string")
            sys.exit()
    except socket.gaierror:
            print("error regarding the host")
            sys.exit()
if host=="-p --open":
    try:
        host2=(input("choose the host to scan (-p --open confirmed):",))
        t2=socket.gethostbyname(host2)
        print(f"IP confirmed: ",t2)
        port_comm_open(host2)
    except socket.gaierror:
            print("error regarding the host")
            sys.exit()
            
if host == "-s":
        percor=(input("Enter the path of the file to be scanned with .txt extension: ",))
        sito_open(percor)
        
else:
    try:
        t=socket.gethostbyname(host)
        print(f"IP confirmed: ",t)
    except socket.gaierror:
            print("error regarding the host")
            sys.exit()
    
    


#CONDIZIONE NEL CASO INPUT <1
while True:
    port1=int(input("start port to scan: ",))
    
    if port1 >= 1:
        break
    else:
        print("start port is minimum 1")
           
           
#CONDIZIONE NEL CASO INPUT >65536
while True:
    port2=int(input("end port to scan: ",))
    if port2 <= 65536:
        break
    else:
        print("there are no more than 65536 port ")
        
end_p=((f"port confirmed: {port1}-{port2}"))
print(end_p)

port_scanner(t,port1,port2)
end=time.time()
dif=start-end
print("_" *25)
print("SCAN COMPLETED")
print(dif)
print("_" *25)






    
    






