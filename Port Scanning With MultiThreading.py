# Multithreaded Port Scanner
# by NeuralNine Copyright (c) 2019
from queue import Queue
import socket
import threading

target = "127.0.0.1"
queue = Queue()
open_ports = []


def portscan(port,url):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.settimeout(2)
        sock.connect((url, port))
        return True
    except:
        return False

def get_ports():
    for port in range(1, 512):
        queue.put(port)
    
def worker(url):
    while not queue.empty():
        port = queue.get()
        if portscan(port,url):
            print("Port {} is open!".format(port))
            open_ports.append(port)

def run_scanner(urls):
    
    url = socket.gethostbyname(urls)
    print(url)
    threads=200
    get_ports()

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker,args=(url,))
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    #print("Open ports are:", open_ports)
    return open_ports

#v=run_scanner("www.kaizerpk.com")
#print(len(v))