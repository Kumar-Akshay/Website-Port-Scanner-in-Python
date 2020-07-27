#!/usr/bin/python3
import socket
import sys
import time
import threading


def port_scan(url):
    start_port = 1
    end_port = 1000
    usage = "Python port_scan Target Start_port End_Port"
    print("-"*70)
    print("Website Port Scanner in Python")
    print("-"*70)

    try:
        target = socket.gethostbyname(url)
        print(target)
    except socket.gaierror:
        print("Name Resolution error")
        sys.exit()
    print("Scanning the Port", target)

    def scan_port(port):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(2)
        conn = s.connect_ex((target,port))
        if(not conn):
            print("Port {} is OPEN".format(port))
        s.close() 
        
    for port in range(start_port,end_port+1):
        thread = threading.Thread(target = scan_port, args= (port,))
        thread.start()    

port_scan("nu.edu.pk")