import socket 
import threading 
import sys 
import pickle 
class Servidor(): 

    """docstring for Servidor""" 
    def __init__(self, host = "localhost", port=9000): 
        self.clientes = [] 
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.sock.bind((str(host), int(port))) 
        print ("ESPERANDO CONEXIONES EN LOCALHOST, PUERTO:", port) 
        self.sock.listen(5) 
        self.sock.setblocking(False) 
procesar 
        aceptar = threading.Thread(target=self.aceptarCon) 
        procesar = threading.Thread(target=self.procesarCon) 
        aceptar.daemon = True  
        aceptar.start() 
        procesar.daemon = True 
        procesar.start() 
        while True: 
            msg = input('->') 
            if msg == 'salir': 
                print("Servidor desconectado")  
                self.sock.close() 
                sys.exit() 
            else: 
                pass 
    def msg_to_all(self, msg, cliente): 
        for c in self.clientes: 
            try: 
debuelva su mismo msj 
                if c != cliente: 
                    c.send(msg) 
            except: 
                self.clientes.remove(c) 
    def aceptarCon(self): 
        while True: 
            try: 
                conn, addr = self.sock.accept() 
                print("CLIENTE CONECTADO")
                conn.setblocking(False) 
                self.clientes.append(conn) 
            except: 
                pass 
    def procesarCon(self): 
        while True: 
            if len(self.clientes) > 0: 
                for c in self.clientes: 
                    try: 
                        data = c.recv(1024) 
                        if data: 
                            self.msg_to_all(data,c) 
                    except: 
                        pass 
s = Servidor() 

