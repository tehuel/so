# 3 threads trabajando la misma estructura de datos
# referencia: http://mundogeek.net/archivos/2008/04/18/threads-en-python/

import threading

lista_lockable = []

lock = threading.Lock()


class reader(threading.Thread):
    
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        
    def run(self):
        lock.acquire()
        
        data = lista_lockable.pop()
        print self.name, " got:", data
        
        lock.release()
        
class adder(threading.Thread):
    
    def __init__(self, name, number):
        threading.Thread.__init__(self)
        self.name = name
        self.number = number
        
    def run(self):
        lock.acquire()
        
        lista_lockable.append( self.number )
        print self.name, " added:", self.number
        
        lock.release()
        
        
class deleter(threading.Thread):
    
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        
    def run(self):
        lock.acquire()
        
        data = lista_lockable.pop()
        print self.name, " deleted:", data
        
        lock.release()
        

adder_1 = adder("Adder1", 1)
adder_2 = adder("Adder2", 2)

deleter_1 = deleter("Deleter1")
deleter_2 = deleter("Deleter2")

reader_1 = reader("Reader1")
reader_2 = reader("Reader2")


adder_1.start()
adder_2.start()
reader_1.start()
deleter_1.start()


adder_1.join()
reader_1.join()
adder_2.join()
deleter_1.join()
